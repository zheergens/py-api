reload = True

# bind = 'unix:/var/run/d2admin/gunicorn_tool.sock'
bind = '0.0.0.0:3000'

workers = 2

loglevel = 'warning'
backlog = 2048
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
worker_connections = 2000
timeout = 600

daemon = True

pidfile = '/var/run/erp-api.pid'
capture_output = True

access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s" "%(T)s"'
accesslog = '/var/log/erp-api/gunicorn_access.log'
errorlog = '/var/log/erp-api/gunicorn_error.log'
