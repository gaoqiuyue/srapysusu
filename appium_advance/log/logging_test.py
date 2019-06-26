import logging
##只会属于》=info级别的信息，debug的不输出,filename---定义日志输出文件（控制台不打印了）
logging.basicConfig(level=logging.INFO,filename="runlog.log",\
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
logging.debug("debuginfo")
logging.info("info")
logging.warning("warninfo")
logging.error("errorinfo")
logging.critical("criticalinfo")