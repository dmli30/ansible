readTemplate("/home/weblogic/Oracle/Middleware/Oracle_Home/wlserver/common/templates/wls/wls.jar")

cd('Servers/AdminServer')
set('ListenAddress','{{ ansible_default_ipv4["address"] }}')
set('ListenPort', 7001)

cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('{{ weblogic_console_passwd }}')

setOption('OverwriteDomain', 'true')
setOption('JavaHome', '{{ JAVA_HOME }}')
writeDomain('/home/weblogic/Oracle/Middleware/Oracle_Home/user_projects/domains/{{ domain_name }}')

closeTemplate()

exit()
