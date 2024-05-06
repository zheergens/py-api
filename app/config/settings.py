class LoggerConfig:
    INFO_LOG = "/var/log/erp-api/info.log"
    ERROR_LOG = "/var/log/erp-api/error.log"
    SLOW_ACTION = "/var/log/erp-api/slow.log"
    LEVEL_INFO = 1


class DBConfig:
    HOST = "127.0.0.1"
    PORT = 27017
    DB = "ERP"
