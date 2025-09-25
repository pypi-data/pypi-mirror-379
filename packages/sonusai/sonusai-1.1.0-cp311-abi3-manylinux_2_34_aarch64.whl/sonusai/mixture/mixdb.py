# ruff: noqa: S608
from functools import cached_property
from functools import lru_cache
from functools import partial
from typing import Any

from ..datatypes import ASRConfigs
from ..datatypes import AudioF
from ..datatypes import AudioT
from ..datatypes import ClassCount
from ..datatypes import Feature
from ..datatypes import FeatureGeneratorConfig
from ..datatypes import FeatureGeneratorInfo
from ..datatypes import GeneralizedIDs
from ..datatypes import ImpulseResponseFile
from ..datatypes import MetricDoc
from ..datatypes import MetricDocs
from ..datatypes import Mixture
from ..datatypes import Segsnr
from ..datatypes import SourceFile
from ..datatypes import Sources
from ..datatypes import SourcesAudioF
from ..datatypes import SourcesAudioT
from ..datatypes import SpectralMask
from ..datatypes import SpeechMetadata
from ..datatypes import TransformConfig
from ..datatypes import TruthConfigs
from ..datatypes import TruthDict
from ..datatypes import TruthsConfigs
from ..datatypes import TruthsDict
from ..datatypes import UniversalSNR
from .db import SQLiteDatabase
from .db import db_file


class MixtureDatabase:
    def __init__(
        self,
        location: str,
        test: bool = False,
        verbose: bool = False,
        use_cache: bool = True,
    ) -> None:
        self.location = location
        self.test = test
        self.db_path = db_file(location=self.location, test=self.test)
        self.verbose = verbose
        self.use_cache = use_cache

        self.db = partial(SQLiteDatabase, location=self.location, test=self.test, verbose=self.verbose)

        # Update ASR configs
        self.update_asr_configs()

    def update_asr_configs(self) -> None:
        """Update the asr_configs column in the top table with the current asr_configs in the config.yml file."""
        import json

        from ..config.config import load_config

        # Check config.yml to see if asr_configs has changed and update the database if needed
        config = load_config(self.location)
        new_asr_configs = json.dumps(config["asr_configs"])
        with SQLiteDatabase(
                location=self.location,
                readonly=False,
                test=self.test,
                verbose=self.verbose,
        ) as c:
            old_asr_configs = c.execute("SELECT asr_configs FROM top").fetchone()

            if old_asr_configs is not None and new_asr_configs != old_asr_configs[0]:
                c.execute("UPDATE top SET asr_configs = ? WHERE ? = id", (new_asr_configs,))

    @cached_property
    def json(self) -> str:
        from ..datatypes import MixtureDatabaseConfig

        config = MixtureDatabaseConfig(
            asr_configs=self.asr_configs,
            class_balancing=self.class_balancing,
            class_labels=self.class_labels,
            class_weights_threshold=self.class_weights_thresholds,
            feature=self.feature,
            ir_files=self.ir_files,
            mixtures=self.mixtures,
            num_classes=self.num_classes,
            spectral_masks=self.spectral_masks,
            source_files=self.source_files,
        )
        return config.to_json(indent=2)

    def save(self) -> None:
        """Save the MixtureDatabase as a JSON file"""
        from os.path import join

        json_name = join(self.location, "mixdb.json")
        with open(file=json_name, mode="w") as file:
            file.write(self.json)

    @cached_property
    def fg_config(self) -> FeatureGeneratorConfig:
        return FeatureGeneratorConfig(
            feature_mode=self.feature,
            truth_parameters=self.truth_parameters,
        )

    @cached_property
    def fg_info(self) -> FeatureGeneratorInfo:
        from .helpers import get_feature_generator_info

        return get_feature_generator_info(self.fg_config)

    @cached_property
    def truth_parameters(self) -> dict[str, dict[str, int | None]]:
        with self.db() as c:
            rows = c.execute("SELECT category, name, parameters FROM truth_parameters").fetchall()
            truth_parameters: dict[str, dict[str, int | None]] = {}
            for row in rows:
                category, name, parameters = row
                if category not in truth_parameters:
                    truth_parameters[category] = {}
                truth_parameters[category][name] = parameters
            return truth_parameters

    @cached_property
    def num_classes(self) -> int:
        with self.db() as c:
            return int(c.execute("SELECT num_classes FROM top").fetchone()[0])

    @cached_property
    def asr_configs(self) -> ASRConfigs:
        import json

        with self.db() as c:
            return json.loads(c.execute("SELECT asr_configs FROM top").fetchone()[0])

    @cached_property
    def supported_metrics(self) -> MetricDocs:
        metrics = MetricDocs(
            [
                MetricDoc("Mixture Metrics", "mxsnr", "SNR specification in dB"),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnr_avg",
                    "Segmental SNR average over all frames",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnr_std",
                    "Segmental SNR standard deviation over all frames",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnrdb_avg",
                    "Segmental SNR average of the dB frame values over all frames",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnrdb_std",
                    "Segmental SNR standard deviation of the dB frame values over all frames",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnrf_avg",
                    "Per-bin segmental SNR average over all frames (using feature transform)",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnrf_std",
                    "Per-bin segmental SNR standard deviation over all frames (using feature transform)",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnrdbf_avg",
                    "Per-bin segmental average of the dB frame values over all frames (using feature transform)",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxssnrdbf_std",
                    "Per-bin segmental standard deviation of the dB frame values over all frames (using feature transform)",
                ),
                MetricDoc("Mixture Metrics", "mxpesq", "PESQ of mixture versus true sources"),
                MetricDoc(
                    "Mixture Metrics",
                    "mxwsdr",
                    "Weighted signal distortion ratio of mixture versus true sources",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxpd",
                    "Phase distance between mixture and true sources",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxstoi",
                    "Short term objective intelligibility of mixture versus true sources",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxcsig",
                    "Predicted rating of speech distortion of mixture versus true sources",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxcbak",
                    "Predicted rating of background distortion of mixture versus true sources",
                ),
                MetricDoc(
                    "Mixture Metrics",
                    "mxcovl",
                    "Predicted rating of overall quality of mixture versus true sources",
                ),
                MetricDoc("Mixture Metrics", "ssnr", "Segmental SNR"),
                MetricDoc("Mixture Metrics", "mxdco", "Mixture DC offset"),
                MetricDoc("Mixture Metrics", "mxmin", "Mixture min level"),
                MetricDoc("Mixture Metrics", "mxmax", "Mixture max levl"),
                MetricDoc("Mixture Metrics", "mxpkdb", "Mixture Pk lev dB"),
                MetricDoc("Mixture Metrics", "mxlrms", "Mixture RMS lev dB"),
                MetricDoc("Mixture Metrics", "mxpkr", "Mixture RMS Pk dB"),
                MetricDoc("Mixture Metrics", "mxtr", "Mixture RMS Tr dB"),
                MetricDoc("Mixture Metrics", "mxcr", "Mixture Crest factor"),
                MetricDoc("Mixture Metrics", "mxfl", "Mixture Flat factor"),
                MetricDoc("Mixture Metrics", "mxpkc", "Mixture Pk count"),
                MetricDoc("Sources Metrics", "sdco", "Sources DC offset"),
                MetricDoc("Sources Metrics", "smin", "Sources min level"),
                MetricDoc("Sources Metrics", "smax", "Sources max levl"),
                MetricDoc("Sources Metrics", "spkdb", "Sources Pk lev dB"),
                MetricDoc("Sources Metrics", "slrms", "Sources RMS lev dB"),
                MetricDoc("Sources Metrics", "spkr", "Sources RMS Pk dB"),
                MetricDoc("Sources Metrics", "str", "Sources RMS Tr dB"),
                MetricDoc("Sources Metrics", "scr", "Sources Crest factor"),
                MetricDoc("Sources Metrics", "sfl", "Sources Flat factor"),
                MetricDoc("Sources Metrics", "spkc", "Sources Pk count"),
                MetricDoc("Source Metrics", "mxsdco", "Source DC offset"),
                MetricDoc("Source Metrics", "mxsmin", "Source min level"),
                MetricDoc("Source Metrics", "mxsmax", "Source max levl"),
                MetricDoc("Source Metrics", "mxspkdb", "Source Pk lev dB"),
                MetricDoc("Source Metrics", "mxslrms", "Source RMS lev dB"),
                MetricDoc("Source Metrics", "mxspkr", "Source RMS Pk dB"),
                MetricDoc("Source Metrics", "mxstr", "Source RMS Tr dB"),
                MetricDoc("Source Metrics", "mxscr", "Source Crest factor"),
                MetricDoc("Source Metrics", "mxsfl", "Source Flat factor"),
                MetricDoc("Source Metrics", "mxspkc", "Source Pk count"),
                MetricDoc("Noise Metrics", "ndco", "Noise DC offset"),
                MetricDoc("Noise Metrics", "nmin", "Noise min level"),
                MetricDoc("Noise Metrics", "nmax", "Noise max levl"),
                MetricDoc("Noise Metrics", "npkdb", "Noise Pk lev dB"),
                MetricDoc("Noise Metrics", "nlrms", "Noise RMS lev dB"),
                MetricDoc("Noise Metrics", "npkr", "Noise RMS Pk dB"),
                MetricDoc("Noise Metrics", "ntr", "Noise RMS Tr dB"),
                MetricDoc("Noise Metrics", "ncr", "Noise Crest factor"),
                MetricDoc("Noise Metrics", "nfl", "Noise Flat factor"),
                MetricDoc("Noise Metrics", "npkc", "Noise Pk count"),
                MetricDoc(
                    "Truth Metrics",
                    "sedavg",
                    "(not implemented) Average SED activity over all frames [truth_parameters, 1]",
                ),
                MetricDoc(
                    "Truth Metrics",
                    "sedcnt",
                    "(not implemented) Count in number of frames that SED is active [truth_parameters, 1]",
                ),
                MetricDoc(
                    "Truth Metrics",
                    "sedtop3",
                    "(not implemented) 3 most active by largest sedavg [3, 1]",
                ),
                MetricDoc(
                    "Truth Metrics",
                    "sedtopn",
                    "(not implemented) N most active by largest sedavg [N, 1]",
                ),
            ]
        )
        for name in self.asr_configs:
            metrics.append(
                MetricDoc(
                    "Source Metrics",
                    f"mxsasr.{name}",
                    f"Source ASR text using {name} ASR as defined in mixdb asr_configs parameter",
                )
            )
            metrics.append(
                MetricDoc(
                    "Sources Metrics",
                    f"sasr.{name}",
                    f"Sources ASR text using {name} ASR as defined in mixdb asr_configs parameter",
                )
            )
            metrics.append(
                MetricDoc(
                    "Mixture Metrics",
                    f"mxasr.{name}",
                    f"ASR text using {name} ASR as defined in mixdb asr_configs parameter",
                )
            )
            metrics.append(
                MetricDoc(
                    "Sources Metrics",
                    f"basewer.{name}",
                    f"Word error rate of sasr.{name} vs. speech text metadata for the source",
                )
            )
            metrics.append(
                MetricDoc(
                    "Mixture Metrics",
                    f"mxwer.{name}",
                    f"Word error rate of mxasr.{name} vs. sasr.{name}",
                )
            )

        return metrics

    @cached_property
    def class_balancing(self) -> bool:
        with self.db() as c:
            return bool(c.execute("SELECT class_balancing FROM top").fetchone()[0])

    @cached_property
    def feature(self) -> str:
        with self.db() as c:
            return str(c.execute("SELECT feature FROM top").fetchone()[0])

    @cached_property
    def fg_decimation(self) -> int:
        return self.fg_info.decimation

    @cached_property
    def fg_stride(self) -> int:
        return self.fg_info.stride

    @cached_property
    def fg_step(self) -> int:
        return self.fg_info.step

    @cached_property
    def feature_parameters(self) -> int:
        return self.fg_info.feature_parameters

    @cached_property
    def ft_config(self) -> TransformConfig:
        return self.fg_info.ft_config

    @cached_property
    def eft_config(self) -> TransformConfig:
        return self.fg_info.eft_config

    @cached_property
    def it_config(self) -> TransformConfig:
        return self.fg_info.it_config

    @cached_property
    def transform_frame_ms(self) -> float:
        from ..constants import SAMPLE_RATE

        return float(self.ft_config.overlap) / float(SAMPLE_RATE / 1000)

    @cached_property
    def feature_ms(self) -> float:
        return self.transform_frame_ms * self.fg_decimation * self.fg_stride

    @cached_property
    def feature_samples(self) -> int:
        return self.ft_config.overlap * self.fg_decimation * self.fg_stride

    @cached_property
    def feature_step_ms(self) -> float:
        return self.transform_frame_ms * self.fg_decimation * self.fg_step

    @cached_property
    def feature_step_samples(self) -> int:
        return self.ft_config.overlap * self.fg_decimation * self.fg_step

    def total_samples(self, m_ids: GeneralizedIDs = "*") -> int:
        return sum([self.mixture(m_id).samples for m_id in self.mixids_to_list(m_ids)])

    def total_transform_frames(self, m_ids: GeneralizedIDs = "*") -> int:
        return self.total_samples(m_ids) // self.ft_config.overlap

    def total_feature_frames(self, m_ids: GeneralizedIDs = "*") -> int:
        return self.total_samples(m_ids) // self.feature_step_samples

    def mixture_transform_frames(self, m_id: int) -> int:
        from .helpers import frames_from_samples

        return frames_from_samples(self.mixture(m_id).samples, self.ft_config.overlap)

    def mixture_feature_frames(self, m_id: int) -> int:
        from .helpers import frames_from_samples

        return frames_from_samples(self.mixture(m_id).samples, self.feature_step_samples)

    def mixids_to_list(self, m_ids: GeneralizedIDs = "*") -> list[int]:
        """Resolve generalized mixture IDs to a list of integers

        :param m_ids: Generalized mixture IDs
        :return: List of mixture ID integers
        """
        from .helpers import generic_ids_to_list

        return generic_ids_to_list(self.num_mixtures, m_ids)

    @cached_property
    def class_labels(self) -> list[str]:
        """Get class labels from db

        :return: Class labels
        """
        with self.db() as c:
            return [str(item[0]) for item in c.execute("SELECT label FROM class_label ORDER BY id").fetchall()]

    @cached_property
    def class_weights_thresholds(self) -> list[float]:
        """Get class weights thresholds from db

        :return: Class weights thresholds
        """
        with self.db() as c:
            return [float(item[0]) for item in c.execute("SELECT threshold FROM class_weights_threshold").fetchall()]

    def category_truth_configs(self, category: str) -> dict[str, str]:
        return _category_truth_configs(self.db, category, self.use_cache)

    def source_truth_configs(self, s_id: int) -> TruthConfigs:
        return _source_truth_configs(self.db, s_id, self.use_cache)

    def mixture_truth_configs(self, m_id: int) -> TruthsConfigs:
        mixture = self.mixture(m_id)
        return {
            category: self.source_truth_configs(mixture.all_sources[category].file_id)
            for category in mixture.all_sources
        }

    @cached_property
    def random_snrs(self) -> list[float]:
        """Get random snrs from db

        :return: Random SNRs
        """
        with self.db() as c:
            return list(
                {float(item[0]) for item in c.execute("SELECT snr FROM source WHERE snr_random == 1").fetchall()}
            )

    @cached_property
    def snrs(self) -> list[float]:
        """Get snrs from db

        :return: SNRs
        """
        with self.db() as c:
            return list(
                {float(item[0]) for item in c.execute("SELECT snr FROM source WHERE snr_random == 0").fetchall()}
            )

    @cached_property
    def all_snrs(self) -> list[UniversalSNR]:
        return sorted(
            set(
                [UniversalSNR(is_random=False, value=snr) for snr in self.snrs]
                + [UniversalSNR(is_random=True, value=snr) for snr in self.random_snrs]
            )
        )

    @cached_property
    def spectral_masks(self) -> list[SpectralMask]:
        """Get spectral masks from db

        :return: Spectral masks
        """
        from .db_datatypes import SpectralMaskRecord

        with self.db() as c:
            spectral_masks = [
                SpectralMaskRecord(*result) for result in c.execute("SELECT * FROM spectral_mask").fetchall()
            ]
            return [
                SpectralMask(
                    f_max_width=spectral_mask.f_max_width,
                    f_num=spectral_mask.f_num,
                    t_max_width=spectral_mask.t_max_width,
                    t_num=spectral_mask.t_num,
                    t_max_percent=spectral_mask.t_max_percent,
                )
                for spectral_mask in spectral_masks
            ]

    def spectral_mask(self, sm_id: int) -> SpectralMask:
        """Get spectral mask with ID from db

        :param sm_id: Spectral mask ID
        :return: Spectral mask
        """
        return _spectral_mask(self.db, sm_id, self.use_cache)

    @cached_property
    def source_files(self) -> dict[str, list[SourceFile]]:
        """Get source files from db

        :return: Source files
        """
        import json

        from ..datatypes import TruthConfig
        from ..datatypes import TruthConfigs
        from .db_datatypes import SourceFileRecord

        with self.db() as c:
            source_files: dict[str, list[SourceFile]] = {}
            categories = c.execute("SELECT DISTINCT category FROM source_file").fetchall()
            for category in categories:
                source_files[category[0]] = []
                source_file_records = [
                    SourceFileRecord(*result)
                    for result in c.execute("SELECT * FROM source_file WHERE ? = category", (category[0],)).fetchall()
                ]
                for source_file_record in source_file_records:
                    truth_configs: TruthConfigs = {}
                    for truth_config_records in c.execute(
                        """
                        SELECT truth_config.config
                        FROM truth_config, source_file_truth_config
                        WHERE ? = source_file_truth_config.source_file_id
                        AND truth_config.id = source_file_truth_config.truth_config_id
                        """,
                        (source_file_record.id,),
                    ).fetchall():
                        truth_config = json.loads(truth_config_records[0])
                        truth_configs[truth_config["name"]] = TruthConfig(
                            function=truth_config["function"],
                            stride_reduction=truth_config["stride_reduction"],
                            config=truth_config["config"],
                        )
                    source_files[source_file_record.category].append(
                        SourceFile(
                            id=source_file_record.id,
                            category=source_file_record.category,
                            name=source_file_record.name,
                            samples=source_file_record.samples,
                            class_indices=json.loads(source_file_record.class_indices),
                            level_type=source_file_record.level_type,
                            truth_configs=truth_configs,
                            speaker_id=source_file_record.speaker_id,
                        )
                    )
            return source_files

    @cached_property
    def source_file_ids(self) -> dict[str, list[int]]:
        """Get source file IDs from db

        :return: Dictionary of a list of source file IDs
        """
        with self.db() as c:
            source_file_ids: dict[str, list[int]] = {}
            categories = c.execute("SELECT DISTINCT category FROM source_file").fetchall()
            for category in categories:
                source_file_ids[category[0]] = [
                    int(item[0])
                    for item in c.execute("SELECT id FROM source_file WHERE ? = category", (category[0],)).fetchall()
                ]
            return source_file_ids

    def source_file(self, s_id: int) -> SourceFile:
        """Get the source file with ID from db

        :param s_id: Source file ID
        :return: Source file
        """
        return _source_file(self.db, s_id, self.use_cache)

    def num_source_files(self, category: str) -> int:
        """Get the number of source files from the category from db

        :param category: Source category
        :return: Number of source files
        """
        return _num_source_files(self.db, category, self.use_cache)

    @cached_property
    def ir_files(self) -> list[ImpulseResponseFile]:
        """Get impulse response files from db

        :return: Impulse response files
        """
        from .db_datatypes import ImpulseResponseFileRecord

        with self.db() as c:
            files: list[ImpulseResponseFile] = []
            entries = c.execute("SELECT * FROM ir_file").fetchall()
            for entry in entries:
                file = ImpulseResponseFileRecord(*entry)

                tags = [
                    tag[0]
                    for tag in c.execute(
                        """
                SELECT ir_tag.tag
                FROM ir_tag, ir_file_ir_tag
                WHERE ? = ir_file_ir_tag.file_id
                AND ir_tag.id = ir_file_ir_tag.tag_id
                """,
                        (file.id,),
                    ).fetchall()
                ]

                files.append(
                    ImpulseResponseFile(
                        delay=file.delay,
                        name=file.name,
                        tags=tags,
                    )
                )

        return files

    @cached_property
    def ir_file_ids(self) -> list[int]:
        """Get impulse response file IDs from db

        :return: List of impulse response file IDs
        """
        with self.db() as c:
            return [int(item[0]) for item in c.execute("SELECT id FROM ir_file").fetchall()]

    def ir_file_ids_for_tag(self, tag: str) -> list[int]:
        """Get impulse response file IDs for the given tag from db

        :return: List of impulse response file IDs for the given tag
        """
        with self.db() as c:
            tag_id = c.execute("SELECT id FROM ir_tag WHERE ? = tag", (tag,)).fetchone()
            if not tag_id:
                return []

            return [
                int(item[0] - 1)
                for item in c.execute("SELECT file_id FROM ir_file_ir_tag WHERE ? = tag_id", (tag_id[0],)).fetchall()
            ]

    def ir_file(self, ir_id: int) -> str:
        """Get impulse response file name with ID from db

        :param ir_id: Impulse response file ID
        :return: Impulse response file name
        """
        return _ir_file(self.db, ir_id, self.use_cache)

    def ir_delay(self, ir_id: int) -> int:
        """Get impulse response delay with ID from db

        :param ir_id: Impulse response file ID
        :return: Impulse response delay
        """
        return _ir_delay(self.db, ir_id, self.use_cache)

    @cached_property
    def num_ir_files(self) -> int:
        """Get number of impulse response files from db

        :return: Number of impulse response files
        """
        with self.db() as c:
            return int(c.execute("SELECT count(id) FROM ir_file").fetchone()[0])

    @cached_property
    def ir_tags(self) -> list[str]:
        """Get tags of impulse response files from db

        :return: Tags of impulse response files
        """
        with self.db() as c:
            return [tag[0] for tag in c.execute("SELECT tag FROM ir_tag").fetchall()]

    @property
    def mixtures(self) -> list[Mixture]:
        """Get mixtures from db

        :return: Mixtures
        """
        from .db_datatypes import MixtureRecord
        from .db_datatypes import SourceRecord
        from .helpers import to_mixture
        from .helpers import to_source

        with self.db() as c:
            mixtures: list[Mixture] = []
            for mixture in [MixtureRecord(*record) for record in c.execute("SELECT * FROM mixture").fetchall()]:
                sources_list = [
                    to_source(SourceRecord(*source))
                    for source in c.execute(
                        """
                        SELECT source.*
                        FROM source, mixture_source
                        WHERE ? = mixture_source.mixture_id AND source.id = mixture_source.source_id
                        """,
                        (mixture.id,),
                    ).fetchall()
                ]

                sources: Sources = {}
                for source in sources_list:
                    sources[self.source_file(source.file_id).category] = source

                mixtures.append(to_mixture(mixture, sources))

        return mixtures

    @cached_property
    def mixture_ids(self) -> list[int]:
        """Get mixture IDs from db

        :return: List of zero-based mixture IDs
        """
        with self.db() as c:
            return [int(item[0]) - 1 for item in c.execute("SELECT id FROM mixture").fetchall()]

    def mixture(self, m_id: int) -> Mixture:
        """Get mixture record with ID from db

        :param m_id: Zero-based mixture ID
        :return: Mixture record
        """
        return _mixture(self.db, m_id, self.use_cache)

    @cached_property
    def mixid_width(self) -> int:
        with self.db() as c:
            return int(c.execute("SELECT mixid_width FROM top").fetchone()[0])

    def mixture_location(self, m_id: int) -> str:
        """Get the file location for the give mixture ID

        :param m_id: Zero-based mixture ID
        :return: File location
        """
        from os.path import join

        return join(self.location, self.mixture(m_id).name)

    @cached_property
    def num_mixtures(self) -> int:
        """Get the number of mixtures from db

        :return: Number of mixtures
        """
        with self.db() as c:
            return int(c.execute("SELECT count(id) FROM mixture").fetchone()[0])

    def read_mixture_data(self, m_id: int, items: list[str] | str) -> dict[str, Any]:
        """Read mixture data

        :param m_id: Zero-based mixture ID
        :param items: String(s) of dataset(s) to retrieve
        :return: Dictionary of name: data
        """
        from .data_io import read_cached_data

        return read_cached_data(self.location, "mixture", self.mixture(m_id).name, items)

    def read_source_audio(self, s_id: int) -> AudioT:
        """Read source audio

        :param s_id: Source ID
        :return: Source audio
        """
        from .audio import read_audio

        return read_audio(self.source_file(s_id).name, self.use_cache)

    def mixture_class_indices(self, m_id: int) -> list[int]:
        class_indices: list[int] = []
        for s_id in self.mixture(m_id).source_ids.values():
            class_indices.extend(self.source_file(s_id).class_indices)
        return sorted(set(class_indices))

    def mixture_sources(self, m_id: int, force: bool = False, cache: bool = False) -> SourcesAudioT:
        """Get the pre-truth source audio data (one per source in the mixture) for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Dictionary of pre-truth source audio data (one per source in the mixture)
        """
        from .data_io import write_cached_data
        from .effects import apply_effects
        from .effects import conform_audio_to_length

        if not force:
            sources = self.read_mixture_data(m_id, "sources")["sources"]
            if sources is not None:
                return sources

        mixture = self.mixture(m_id)
        if mixture is None:
            raise ValueError(f"Could not find mixture for m_id: {m_id}")

        sources = {}
        for category, source in mixture.all_sources.items():
            source = mixture.all_sources[category]
            audio = self.read_source_audio(source.file_id)
            audio = apply_effects(self, audio, source.effects, pre=True, post=False)
            audio = conform_audio_to_length(audio, mixture.samples, source.loop, source.start)
            sources[category] = audio

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=mixture.name,
                items={"sources": sources},
            )

        return sources

    def mixture_sources_f(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> SourcesAudioF:
        """Get the pre-truth source transform data (one per source in the mixture) for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Dictionary of pre-truth source transform data (one per source in the mixture)
        """
        from .data_io import write_cached_data
        from .helpers import forward_transform

        if sources is None:
            sources = self.mixture_sources(m_id, force)

        sources_f = {category: forward_transform(sources[category], self.ft_config) for category in sources}

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"sources_f": sources_f},
            )

        return sources_f

    def mixture_source(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> AudioT:
        """Get the post-truth, summed, and gained source audio data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Post-truth, gained, and summed source audio data
        """
        import numpy as np

        from .data_io import write_cached_data
        from .effects import apply_effects

        if not force:
            source = self.read_mixture_data(m_id, "source")["source"]
            if source is not None:
                return source

        if sources is None:
            sources = self.mixture_sources(m_id, force)

        mixture = self.mixture(m_id)

        source = np.sum(
            [
                apply_effects(
                    self,
                    audio=sources[category],
                    effects=mixture.all_sources[category].effects,
                    pre=False,
                    post=True,
                )
                * mixture.all_sources[category].snr_gain
                for category in sources
                if category != "noise"
            ],
            axis=0,
        )

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=mixture.name,
                items={"source": source},
            )

        return source

    def mixture_source_f(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        source: AudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> AudioF:
        """Get the post-truth, summed, and gained source transform data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param source: Post-truth, gained, and summed source audio for the given m_id
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Post-truth, gained, and summed source transform data
        """
        from .data_io import write_cached_data
        from .helpers import forward_transform

        if source is None:
            source = self.mixture_source(m_id, sources, force)

        source_f = forward_transform(source, self.ft_config)

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"source_f": source_f},
            )

        return source_f

    def mixture_noise(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> AudioT:
        """Get the post-truth and gained noise audio data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Post-truth and gained noise audio data
        """
        from .data_io import write_cached_data
        from .effects import apply_effects

        if not force:
            noise = self.read_mixture_data(m_id, "noise")["noise"]
            if noise is not None:
                return noise

        if sources is None:
            sources = self.mixture_sources(m_id, force)

        noise = self.mixture(m_id).noise
        noise = apply_effects(self, sources["noise"], noise.effects, pre=False, post=True) * noise.snr_gain

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"noise": noise},
            )

        return noise

    def mixture_noise_f(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        noise: AudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> AudioF:
        """Get the post-truth and gained noise transform for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param noise: Post-truth and gained noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Post-truth and gained noise transform data
        """
        from .data_io import write_cached_data
        from .helpers import forward_transform

        if force or noise is None:
            noise = self.mixture_noise(m_id, sources, force)

        noise_f = forward_transform(noise, self.ft_config)
        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"noise_f": noise_f},
            )

        return noise_f

    def mixture_mixture(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        source: AudioT | None = None,
        noise: AudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> AudioT:
        """Get the mixture audio data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param source: Post-truth, gained, and summed source audio data
        :param noise: Post-truth and gained noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Mixture audio data
        """
        from .data_io import write_cached_data

        if not force:
            mixture = self.read_mixture_data(m_id, "mixture")["mixture"]
            if mixture is not None:
                return mixture

        if source is None:
            source = self.mixture_source(m_id, sources, force)

        if noise is None:
            noise = self.mixture_noise(m_id, sources, force)

        mixture = source + noise

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"mixture": mixture},
            )

        return mixture

    def mixture_mixture_f(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        source: AudioT | None = None,
        noise: AudioT | None = None,
        mixture: AudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> AudioF:
        """Get the mixture transform for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param source: Post-truth, gained, and summed source audio data
        :param noise: Post-truth and gained noise audio data
        :param mixture: Mixture audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Mixture transform data
        """
        from .data_io import write_cached_data
        from .helpers import forward_transform
        from .spectral_mask import apply_spectral_mask

        if mixture is None:
            mixture = self.mixture_mixture(m_id, sources, source, noise, force)

        mixture_f = forward_transform(mixture, self.ft_config)

        m = self.mixture(m_id)
        if m.spectral_mask_id is not None:
            mixture_f = apply_spectral_mask(
                audio_f=mixture_f,
                spectral_mask=self.spectral_mask(int(m.spectral_mask_id)),
                seed=m.spectral_mask_seed,
            )

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"mixture_f": mixture_f},
            )

        return mixture_f

    def mixture_truth_t(self, m_id: int, force: bool = False, cache: bool = False) -> TruthsDict:
        """Get the truth_t data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: list of truth_t data
        """
        from .data_io import write_cached_data
        from .truth import truth_function

        if not force:
            truth_t = self.read_mixture_data(m_id, "truth_t")["truth_t"]
            if truth_t is not None:
                return truth_t

        truth_t = truth_function(self, m_id)

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"truth_t": truth_t},
            )

        return truth_t

    def mixture_segsnr_t(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        source: AudioT | None = None,
        noise: AudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> Segsnr:
        """Get the segsnr_t data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param source: Post-truth, gained, and summed source audio data
        :param noise: Post-truth and gained noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: segsnr_t data
        """
        import numpy as np
        import torch
        from pyaaware.torch import ForwardTransform

        from .data_io import write_cached_data

        if not force:
            segsnr_t = self.read_mixture_data(m_id, "segsnr_t")["segsnr_t"]
            if segsnr_t is not None:
                return segsnr_t

        if source is None:
            source = self.mixture_source(m_id, sources, force)

        if noise is None:
            noise = self.mixture_noise(m_id, sources, force)

        ft = ForwardTransform(
            length=self.ft_config.length,
            overlap=self.ft_config.overlap,
            bin_start=self.ft_config.bin_start,
            bin_end=self.ft_config.bin_end,
            ttype=self.ft_config.ttype,
        )

        mixture = self.mixture(m_id)

        segsnr_t = np.empty(mixture.samples, dtype=np.float32)

        source_energy = ft.execute_all(torch.from_numpy(source))[1].numpy()
        noise_energy = ft.execute_all(torch.from_numpy(noise))[1].numpy()

        offsets = range(0, mixture.samples, self.ft_config.overlap)
        if len(source_energy) != len(offsets):
            raise ValueError(
                f"Number of frames in energy, {len(source_energy)}, is not number of frames in mixture, {len(offsets)}"
            )

        for idx, offset in enumerate(offsets):
            indices = slice(offset, offset + self.ft_config.overlap)

            if noise_energy[idx] == 0:
                snr = np.float32(np.inf)
            else:
                snr = np.float32(source_energy[idx] / noise_energy[idx])

            segsnr_t[indices] = snr

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=mixture.name,
                items={"segsnr_t": segsnr_t},
            )

        return segsnr_t

    def mixture_segsnr(
        self,
        m_id: int,
        segsnr_t: Segsnr | None = None,
        sources: SourcesAudioT | None = None,
        source: AudioT | None = None,
        noise: AudioT | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> Segsnr:
        """Get the segsnr data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param segsnr_t: segsnr_t data
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param source: Post-truth, gained, and summed source audio data
        :param noise: Post-truth and gained noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: segsnr data
        """
        from .data_io import write_cached_data

        if not force:
            segsnr = self.read_mixture_data(m_id, "segsnr")["segsnr"]
            if segsnr is not None:
                return segsnr

        if segsnr_t is None:
            segsnr_t = self.mixture_segsnr_t(m_id, sources, source, noise, force)

        segsnr = segsnr_t[0 :: self.ft_config.overlap]

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"segsnr": segsnr},
            )

        return segsnr

    def mixture_ft(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        source: AudioT | None = None,
        noise: AudioT | None = None,
        mixture_f: AudioF | None = None,
        mixture: AudioT | None = None,
        truth_t: TruthsDict | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> tuple[Feature, TruthsDict]:
        """Get the feature and truth_f data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param source: Post-truth, gained, and summed source audio data
        :param noise: Post-truth and gained noise audio data
        :param mixture_f: Mixture transform data
        :param mixture: Mixture audio data
        :param truth_t: truth_t
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Tuple of (feature, truth_f) data
        """
        from pyaaware import FeatureGenerator

        from .data_io import write_cached_data
        from .truth import truth_stride_reduction

        if not force:
            ft = self.read_mixture_data(m_id, ["feature", "truth_f"])
            if ft["feature"] is not None and ft["truth_f"] is not None:
                return ft["feature"], ft["truth_f"]

        if mixture_f is None:
            mixture_f = self.mixture_mixture_f(
                m_id=m_id,
                sources=sources,
                source=source,
                noise=noise,
                mixture=mixture,
                force=force,
            )

        if truth_t is None:
            truth_t = self.mixture_truth_t(m_id, force)

        fg = FeatureGenerator(self.fg_config.feature_mode, self.fg_config.truth_parameters)

        feature, truth_f = fg.execute_tf_all(mixture_f, truth_t)
        if truth_f is None:
            raise TypeError("Unexpected truth of None from feature generator")

        truth_configs = self.mixture_truth_configs(m_id)
        for category, configs in truth_configs.items():
            for name, config in configs.items():
                if self.truth_parameters[category][name] is not None:
                    truth_f[category][name] = truth_stride_reduction(truth_f[category][name], config.stride_reduction)

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"feature": truth_f, "truth_f": truth_f},
            )

        return feature, truth_f

    def mixture_feature(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        noise: AudioT | None = None,
        mixture: AudioT | None = None,
        truth_t: TruthsDict | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> Feature:
        """Get the feature data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param noise: Post-truth and gained noise audio data
        :param mixture: Mixture audio data
        :param truth_t: truth_t
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: Feature data
        """
        from .data_io import write_cached_data

        feature = self.mixture_ft(
            m_id=m_id,
            sources=sources,
            noise=noise,
            mixture=mixture,
            truth_t=truth_t,
            force=force,
        )[0]

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"feature": feature},
            )

        return feature

    def mixture_truth_f(
        self,
        m_id: int,
        sources: SourcesAudioT | None = None,
        noise: AudioT | None = None,
        mixture: AudioT | None = None,
        truth_t: TruthsDict | None = None,
        force: bool = False,
        cache: bool = False,
    ) -> TruthDict:
        """Get the truth_f data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param sources: Dictionary of pre-truth source audio data (one per source in the mixture)
        :param noise: Post-truth and gained noise audio data
        :param mixture: Mixture audio data
        :param truth_t: truth_t
        :param force: Force computing data from original sources regardless of whether cached data exists
        :param cache: Cache result
        :return: truth_f data
        """
        from .data_io import write_cached_data

        truth_f = self.mixture_ft(
            m_id=m_id,
            sources=sources,
            noise=noise,
            mixture=mixture,
            truth_t=truth_t,
            force=force,
        )[1]

        if cache:
            write_cached_data(
                location=self.location,
                name="mixture",
                index=self.mixture(m_id).name,
                items={"truth_f": truth_f},
            )

        return truth_f

    def mixture_class_count(self, m_id: int, truth_t: TruthsDict | None = None) -> dict[str, ClassCount]:
        """Compute the number of frames for which each class index is active for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param truth_t: truth_t
        :return: Dictionary of class counts
        """
        import numpy as np

        if truth_t is None:
            truth_t = self.mixture_truth_t(m_id)

        class_count: dict[str, ClassCount] = {}

        truth_configs = self.mixture_truth_configs(m_id)
        for category in truth_configs:
            class_count[category] = [0] * self.num_classes
            for configs in truth_configs[category]:
                if "sed" in configs:
                    for cl in range(self.num_classes):
                        class_count[category][cl] = int(
                            np.sum(truth_t[category]["sed"][:, cl] >= self.class_weights_thresholds[cl])
                        )

        return class_count

    @cached_property
    def speaker_metadata_tiers(self) -> list[str]:
        import json

        with self.db() as c:
            return json.loads(c.execute("SELECT speaker_metadata_tiers FROM top WHERE 1 = id").fetchone()[0])

    @cached_property
    def textgrid_metadata_tiers(self) -> list[str]:
        import json

        with self.db() as c:
            return json.loads(c.execute("SELECT textgrid_metadata_tiers FROM top WHERE 1 = id").fetchone()[0])

    @cached_property
    def speech_metadata_tiers(self) -> list[str]:
        return sorted(set(self.speaker_metadata_tiers + self.textgrid_metadata_tiers))

    def speaker(self, s_id: int | None, tier: str) -> str | None:
        return _speaker(self.db, s_id, tier, self.use_cache)

    def speech_metadata(self, tier: str) -> list[str]:
        from .helpers import get_textgrid_tier_from_source_file

        results: set[str] = set()
        if tier in self.textgrid_metadata_tiers:
            for source_files in self.source_files.values():
                for source_file in source_files:
                    data = get_textgrid_tier_from_source_file(source_file.name, tier)
                    if data is None:
                        continue
                    if isinstance(data, list):
                        for item in data:
                            results.add(item.label)
                    else:
                        results.add(data)
        elif tier in self.speaker_metadata_tiers:
            for source_files in self.source_files.values():
                for source_file in source_files:
                    data = self.speaker(source_file.speaker_id, tier)
                    if data is not None:
                        results.add(data)

        return sorted(results)

    def mixture_speech_metadata(self, mixid: int, tier: str) -> dict[str, SpeechMetadata]:
        from praatio.utilities.constants import Interval

        from .helpers import get_textgrid_tier_from_source_file

        results: dict[str, SpeechMetadata] = {}
        is_textgrid = tier in self.textgrid_metadata_tiers
        if is_textgrid:
            for category, source in self.mixture(mixid).all_sources.items():
                data = get_textgrid_tier_from_source_file(self.source_file(source.file_id).name, tier)
                if isinstance(data, list):
                    # Check for tempo effect and adjust Interval start and end data as needed
                    entries = []
                    for entry in data:
                        entries.append(
                            Interval(
                                entry.start / source.pre_tempo,
                                entry.end / source.pre_tempo,
                                entry.label,
                            )
                        )
                    results[category] = entries
                else:
                    results[category] = data
        else:
            for category, source in self.mixture(mixid).all_sources.items():
                results[category] = self.speaker(self.source_file(source.file_id).speaker_id, tier)

        return results

    def mixids_for_speech_metadata(
        self,
        tier: str | None = None,
        value: str | None = None,
        where: str | None = None,
    ) -> dict[str, list[int]]:
        """Get a list of mixture IDs for the given speech metadata tier.

        If 'where' is None, then include mixture IDs whose tier values are equal to the given 'value'.
        If 'where' is not None, then ignore 'value' and use the given SQL where clause to determine
        which entries to include.

        Examples:
        >>> mixdb = MixtureDatabase('/mixdb_location')

        >>> mixids = mixdb.mixids_for_speech_metadata('speaker_id', 'TIMIT_ABW0')
        Get mixture IDs for mixtures with speakers whose speaker_ids are 'TIMIT_ABW0'.

        >>> mixids = mixdb.mixids_for_speech_metadata(where='age >= 27')
        Get mixture IDs for mixtures with speakers whose ages are greater than or equal to 27.

        >>> mixids = mixdb.mixids_for_speech_metadata(where="dialect in ('New York City', 'Northern')")
        Get mixture IDs for mixtures with speakers whose dialects are either 'New York City' or 'Northern'.
        """
        if value is None and where is None:
            raise ValueError("Must provide either value or where")

        if where is None:
            if tier is None:
                raise ValueError("Must provide tier")
            where = f"{tier} = '{value}'"

        if tier is not None and tier in self.textgrid_metadata_tiers:
            raise ValueError(f"TextGrid tier data, '{tier}', is not supported in mixids_for_speech_metadata().")

        with self.db() as c:
            results = c.execute(f"SELECT id FROM speaker WHERE {where}").fetchall()
            speaker_ids = ",".join(map(str, [i[0] for i in results]))

            results = c.execute(f"SELECT id, category FROM source_file WHERE speaker_id IN ({speaker_ids})").fetchall()
            source_file_ids: dict[str, list[int]] = {}
            for result in results:
                source_file_id, category = result
                if category not in source_file_ids:
                    source_file_ids[category] = [source_file_id]
                else:
                    source_file_ids[category].append(source_file_id)

            mixids: dict[str, list[int]] = {}
            for category in source_file_ids:
                id_str = ",".join(map(str, source_file_ids[category]))
                results = c.execute(f"SELECT id FROM source WHERE file_id IN ({id_str})").fetchall()
                source_ids = ",".join(map(str, [i[0] for i in results]))

                results = c.execute(
                    f"SELECT mixture_id FROM mixture_source WHERE source_id IN ({source_ids})"
                ).fetchall()
                mixids[category] = [mixture_id[0] - 1 for mixture_id in results]

        return mixids

    def mixture_all_speech_metadata(self, m_id: int) -> dict[str, dict[str, SpeechMetadata]]:
        from .helpers import mixture_all_speech_metadata

        return mixture_all_speech_metadata(self, self.mixture(m_id))

    def cached_metrics(self, m_ids: GeneralizedIDs = "*") -> list[str]:
        """Get a list of cached metrics for all mixtures."""
        from glob import glob
        from os.path import join
        from pathlib import Path

        supported_metrics = self.supported_metrics.names
        first = True
        result: set[str] = set()
        for m_id in self.mixids_to_list(m_ids):
            mixture_dir = join(self.location, "mixture", self.mixture(m_id).name)
            found = {Path(f).stem for f in glob(join(mixture_dir, "*.pkl"))}
            if first:
                first = False
                for f in found:
                    if f in supported_metrics:
                        result.add(f)
            else:
                result = result & found

        return sorted(result)

    def mixture_metrics(self, m_id: int, metrics: list[str], force: bool = False) -> dict[str, Any]:
        """Get metrics data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param metrics: List of metrics to get
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Dictionary of metric data
        """
        from ..metrics import calculate_metrics

        return calculate_metrics(self, m_id, metrics, force)


def _spectral_mask(db: partial, sm_id: int, use_cache: bool = True) -> SpectralMask:
    """Get spectral mask with ID from db

    :param db: Database context
    :param sm_id: Spectral mask ID
    :param use_cache: If true, use LRU caching
    :return: Spectral mask
    """
    if use_cache:
        return __spectral_mask(db, sm_id)
    return __spectral_mask.__wrapped__(db, sm_id)


@lru_cache
def __spectral_mask(db: partial, sm_id: int) -> SpectralMask:
    from .db_datatypes import SpectralMaskRecord

    with db() as c:
        spectral_mask = SpectralMaskRecord(*c.execute("SELECT * FROM spectral_mask WHERE ? = id", (sm_id,)).fetchone())
        return SpectralMask(
            f_max_width=spectral_mask.f_max_width,
            f_num=spectral_mask.f_num,
            t_max_width=spectral_mask.t_max_width,
            t_num=spectral_mask.t_num,
            t_max_percent=spectral_mask.t_max_percent,
        )


def _num_source_files(db: partial, category: str, use_cache: bool = True) -> int:
    """Get the number of source files from a category from db

    :param db: Database context
    :param category: Source category
    :param use_cache: If true, use LRU caching
    :return: Number of source files
    """
    if use_cache:
        return __num_source_files(db, category)
    return __num_source_files.__wrapped__(db, category)


@lru_cache
def __num_source_files(db: partial, category: str) -> int:
    """Get the number of source files from a category from db

    :param db: Database context
    :param category: Source category
    :return: Number of source files
    """
    with db() as c:
        return int(c.execute("SELECT count(id) FROM source_file WHERE ? = category", (category,)).fetchone()[0])


def _source_file(db: partial, s_id: int, use_cache: bool = True) -> SourceFile:
    """Get the source file with ID from db

    :param db: Database context
    :param s_id: Source file ID
    :param use_cache: If true, use LRU caching
    :return: Source file
    """
    if use_cache:
        return __source_file(db, s_id, use_cache)
    return __source_file.__wrapped__(db, s_id, use_cache)


@lru_cache
def __source_file(db: partial, s_id: int, use_cache: bool = True) -> SourceFile:
    """Get the source file with ID from db

    :param db: Database context
    :param s_id: Source file ID
    :param use_cache: If true, use LRU caching
    :return: Source file
    """
    import json

    from .db_datatypes import SourceFileRecord

    with db() as c:
        source_file = SourceFileRecord(*c.execute("SELECT * FROM source_file WHERE ? = id", (s_id,)).fetchone())

        return SourceFile(
            category=source_file.category,
            name=source_file.name,
            samples=source_file.samples,
            class_indices=json.loads(source_file.class_indices),
            level_type=source_file.level_type,
            truth_configs=_source_truth_configs(db, s_id, use_cache),
            speaker_id=source_file.speaker_id,
        )


def _ir_file(db: partial, ir_id: int, use_cache: bool = True) -> str:
    """Get impulse response file name with ID from db

    :param db: Database context
    :param ir_id: Impulse response file ID
    :param use_cache: If true, use LRU caching
    :return: Impulse response file name
    """
    if use_cache:
        return __ir_file(db, ir_id)
    return __ir_file.__wrapped__(db, ir_id)


@lru_cache
def __ir_file(db: partial, ir_id: int) -> str:
    with db() as c:
        return str(c.execute("SELECT name FROM ir_file WHERE ? = id ", (ir_id + 1,)).fetchone()[0])


def _ir_delay(db: partial, ir_id: int, use_cache: bool = True) -> int:
    """Get impulse response delay with ID from db

    :param db: Database context
    :param ir_id: Impulse response file ID
    :param use_cache: If true, use LRU caching
    :return: Impulse response delay
    """
    if use_cache:
        return __ir_delay(db, ir_id)
    return __ir_delay.__wrapped__(db, ir_id)


@lru_cache
def __ir_delay(db: partial, ir_id: int) -> int:
    with db() as c:
        return int(c.execute("SELECT delay FROM ir_file WHERE ? = id", (ir_id + 1,)).fetchone()[0])


def _mixture(db: partial, m_id: int, use_cache: bool = True) -> Mixture:
    """Get mixture record with ID from db

    :param db: Database context
    :param m_id: Zero-based mixture ID
    :param use_cache: If true, use LRU caching
    :return: Mixture record
    """
    if use_cache:
        return __mixture(db, m_id)
    return __mixture.__wrapped__(db, m_id)


@lru_cache
def __mixture(db: partial, m_id: int) -> Mixture:
    from .db_datatypes import MixtureRecord
    from .db_datatypes import SourceRecord
    from .helpers import to_mixture
    from .helpers import to_source

    with db() as c:
        mixture = MixtureRecord(*c.execute("SELECT * FROM mixture WHERE ? = id", (m_id + 1,)).fetchone())

        sources: Sources = {}
        for source in c.execute(
            """
                SELECT source.*
                FROM source, mixture_source
                WHERE ? = mixture_source.mixture_id AND source.id = mixture_source.source_id
                """,
            (mixture.id,),
        ).fetchall():
            s = SourceRecord(*source)
            category = c.execute("SELECT category FROM source_file WHERE ? = id", (s.file_id,)).fetchone()[0]
            sources[category] = to_source(s)

    return to_mixture(mixture, sources)


def _speaker(db: partial, s_id: int | None, tier: str, use_cache: bool = True) -> str | None:
    if use_cache:
        return __speaker(db, s_id, tier)
    return __speaker.__wrapped__(db, s_id, tier)


@lru_cache
def __speaker(db: partial, s_id: int | None, tier: str) -> str | None:
    if s_id is None:
        return None

    with db() as c:
        data = c.execute(f"SELECT {tier} FROM speaker WHERE ? = id", (s_id,)).fetchone()
        if data is None:
            return None
        if data[0] is None:
            return None
        return data[0]


def _category_truth_configs(db: partial, category: str, use_cache: bool = True) -> dict[str, str]:
    if use_cache:
        return __category_truth_configs(db, category)
    return __category_truth_configs.__wrapped__(db, category)


@lru_cache
def __category_truth_configs(db: partial, category: str) -> dict[str, str]:
    import json

    truth_configs: dict[str, str] = {}
    with db() as c:
        s_ids = c.execute("SELECT id FROM source_file WHERE ? = category", (category,)).fetchall()

        for s_id in s_ids:
            for truth_config_record in c.execute(
                """
                SELECT truth_config.config
                FROM truth_config, source_file_truth_config
                WHERE ? = source_file_truth_config.source_file_id AND truth_config.id = source_file_truth_config.truth_config_id
                """,
                (s_id[0],),
            ).fetchall():
                truth_config = json.loads(truth_config_record[0])
                truth_configs[truth_config["name"]] = truth_config["function"]
    return truth_configs


def _source_truth_configs(db: partial, s_id: int, use_cache: bool = True) -> TruthConfigs:
    if use_cache:
        return __source_truth_configs(db, s_id)
    return __source_truth_configs.__wrapped__(db, s_id)


@lru_cache
def __source_truth_configs(db: partial, s_id: int) -> TruthConfigs:
    import json

    from ..datatypes import TruthConfig

    truth_configs: TruthConfigs = {}
    with db() as c:
        for truth_config_record in c.execute(
            """
            SELECT truth_config.config
            FROM truth_config, source_file_truth_config
            WHERE ? = source_file_truth_config.source_file_id AND truth_config.id = source_file_truth_config.truth_config_id
            """,
            (s_id,),
        ).fetchall():
            truth_config = json.loads(truth_config_record[0])
            truth_configs[truth_config["name"]] = TruthConfig(
                function=truth_config["function"],
                stride_reduction=truth_config["stride_reduction"],
                config=truth_config["config"],
            )
    return truth_configs
