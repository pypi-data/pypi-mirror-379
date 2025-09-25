import logging

from protein_information_system.helpers.services.services import check_services
import os
import sys

module_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(module_dir)
sys.path.insert(0, module_dir)


def main(config_path='config/config.yaml'):
    from protein_information_system.helpers.config.yaml import read_yaml_config
    conf = read_yaml_config(config_path)

    logger = logging.getLogger("protein_information_system")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Step 1: Import ORM-based logic & check model coherence
    from protein_information_system.sql.model.model import (
        AccessionManager,
        UniProtExtractor,
        PDBExtractor,
        SequenceEmbeddingManager,
        Structure3DiManager,
        GOAnnotationsQueueProcessor
    )

    # Step 2: Check services running

    check_services(conf, logger)

    # Step 3: Run components
    GOAnnotationsQueueProcessor(conf).start()
    AccessionManager(conf).fetch_accessions_from_api()
    AccessionManager(conf).load_accessions_from_csv()
    UniProtExtractor(conf).start()
    PDBExtractor(conf).start()
    SequenceEmbeddingManager(conf).start()
    Structure3DiManager(conf).start()


if __name__ == '__main__':
    main()
