from flask import request
import os, logging

# Setup logger
logger = logging.getLogger('metrics')
logger.setLevel(logging.INFO)
if os.environ.get("DEBUG") == None:
    # Custom formater for production mode
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

def validate ():
    """Validate remote access.
    Return 'False' if the client has a not valid IP
    or the 'key' is incorrect.

    Otherwise returns 'True'.
    """

    user_key = str(request.args.get('key'))
    user_ip  = str(request.remote_addr)

    # Check client's IP
    if not _is_ip_valid():
        logger.warning(user_ip+" [DENIED] Source IP not allowed!")
        return False

    # Check client's key
    if not _is_key_valid():
        logger.warning(user_ip+" [DENIED] Incorrect key: "+user_key)
        return False
        
    return True


def _is_ip_valid ():
    """Check if client IP is valid
    
    The valid IPs can be setted in 'ACCESS_IPS' os env.

    Always returns true if ACCESS_IPS is not defined.
    """
    user_ip  = str(request.remote_addr)

    # Returns true if ACCESS_IPS is not defined
    if os.environ.get("ACCESS_IPS") == None:
        return True

    # Check client IP address
    allowed_ips = os.environ.get("ACCESS_IPS").split(' ')
    if user_ip not in allowed_ips:
        return False

    return True


def _is_key_valid ():
    """Check if key is valid
    
    The key can be setted in 'ACCESS_KEY' os env.

    Always returns true if ACCESS_KEY is not defined.
    """
    user_key = str(request.args.get('key'))

    # Returns true if ACCESS_KEY is not defined
    if os.environ.get("ACCESS_KEY") == None:
        return True

    # Check request's key
    expected_key = os.environ.get("ACCESS_KEY")
    if expected_key != user_key:
        return False
    
    return True

