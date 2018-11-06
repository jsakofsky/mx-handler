# mx-handler

This combination playbook/script checks the NYU MX servers talos email score
and if any are listed as poor, checks to make sure more than one server is in service and then 
modifies the F5 LTM pools to take them out of service. It will always leave at least one server 
in service.
