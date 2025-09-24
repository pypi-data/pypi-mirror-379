.. api_utils:

=========================
Utils *(autoclean.utils)*
=========================

.. currentmodule:: autoclean.utils

Bids
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   bids.step_convert_to_bids
   bids.step_sanitize_id
   bids.step_create_dataset_desc
   bids.step_create_participants_json

Config
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   config.validate_signal_processing_params
   config.validate_eeg_system
   config.hash_and_encode_yaml
   config.decode_compressed_yaml

Database
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   database.set_database_path
   database.get_run_record
   database.manage_database
   database.manage_database_with_audit_protection

Audit
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   audit.get_user_context
   audit.log_database_access
   audit.verify_access_log_integrity
   audit.get_task_file_info
   audit.create_database_backup
   

FileSystem
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   file_system.step_prepare_directories

Logging
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   logging.configure_logger
   logging.message

.. autosummary::
   :toctree: generated/
   :template: autosummary/class.rst
   :nosignatures:

   logging.LogLevel

Montage
-------------------

.. autosummary::
   :toctree: generated/
   :template: autosummary/function.rst
   :nosignatures:

   montage.load_valid_montages
   montage.get_10_20_to_gsn_mapping
   montage.get_gsn_to_10_20_mapping
   montage.convert_channel_names
   montage.get_standard_set_in_montage
   montage.validate_channel_set




