root
    config.json
    .env
    dependencies
    src
        main.py
        extract
            read_files.py
        dq_checks
            null_check.py
            re_duplicate.py
        data_tranformation
            clean_phone_number.py
            date_format.py
            split_address.py
            manage_missing_keys.py
            flattening.py
        load
            load_to_dest.py
        utility
    data
        raw_entries
        faulty_data
        loaded_data