import configparser

# Method to read config file settings
def read_config():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config

def DServ():
  config = read_config()
  ServerID = int(config['DiscordServer']['ServerId'])
  return ServerID

def Logs():
  config = read_config()
  Log_Chat = config['DiscordServer']['log_chat']
  return Log_Chat
  

def API():
  config = read_config()
  domain = config['APISettings']['domain']
  return domain

def Server():
  config = read_config()
  ip = config['ServerSettings']['ip']
  port = int(config['ServerSettings']['port'])
  retry = int(config['ServerSettings']['retry'])
  timeout = int(config['ServerSettings']['timeout'])
  return ip, port, retry, timeout

def Alerts():
  config = read_config()
  alert_check = config['StatusAlerts']['offline_alert']
  alert_channel = int(config['StatusAlerts']['alert_channel'])
  alert_admin = int(config['StatusAlerts']['alert_admin'])
  return alert_check, alert_channel, alert_admin
  

  