#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-
# Copyright [OnePanel]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
####################################################################################################
# Script Name		: apache.py
# Function Summary  : 1 getSettings
#					  2 modifyConfig
# Parameters		: None
# Return Code		: None
# Note				: None
####################################################################################################
# Update History
# Date			  Author			 Reason
# ________________  _________________ ______________________________________________________________
# 2014/05/14		Chen DengYue	   Create
from utils import cfg_get_array, cfg_set_array

config_file='/etc/vsftpd/vsftpd.conf'
delimiter='='

base_configs = {
			'anonymous_enable':        '',
			'local_enable':            '',
			'local_umask':             '',
			'anon_upload_enable':      '',
			'anon_mkdir_write_enable': '',
			'dirmessage_enable':       '',
			'xferlog_enable':          '',
			'connect_from_port_20':    '',
			'chown_upload':            '',
			'chown_username':          '',
			'xferlog_file':            '',
			'xferlog_std_format':      '',
			'idle_session_timeout':    '',
			'data_connection_timeout': '',
			'nopriv_user':             '',
			'async_abor_enable':       '',
			'ascii_upload_enable':     '',
			'ascii_download_enable':   '',
			'ftpd_banner':             '',
			'deny_email_enable':       '',
			'banned_email_file':       '',
			'chroot_list_enable':      '',
			'chroot_list_file':        '',
			'max_clients':             '',
			'message_file':            '',
}
#---------------------------------------------------------------------------------------------------
#Function Name	  : main_process
#Usage			  : 
#Parameters		  : None
#					 
#Return value	  :
#					 1  
#---------------------------------------------------------------------------------------------------
def main_process(self):
    action = self.get_argument('action', '')
    if action == 'getsettings':
        self.write({'code': 0, 'msg': '获取 vsftp 配置信息成功！', 'data': loadVsftpConfigs()})
    elif action == 'mod':
        self.write({'code': 0, 'msg': 'vsftp 服务配置保存成功！','data': modVsftpConfigs(self)})
    return

# 
#---------------------------------------------------------------------------------------------------
#Function Name	  : loadApacheConfigs
#Usage			  : 
#Parameters		  : None
#					 
#Return value	  :
#					 1  array_configs
#---------------------------------------------------------------------------------------------------
def loadVsftpConfigs():
	array_configs=cfg_get_array(config_file,base_configs,delimiter)
	return array_configs
# 
#---------------------------------------------------------------------------------------------------
#Function Name	  : modApacheConfigs
#Usage			  : 
#Parameters		  : None
#					 
#Return value	  :
#					 1 
#---------------------------------------------------------------------------------------------------
def modVsftpConfigs(self):
	result=cfg_set_array(self,config_file,base_configs,delimiter)
	return result
