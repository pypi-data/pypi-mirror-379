import re, hashlib, base64, time, secrets, requests

def digest_client(url, username, password):
    from requests.auth import HTTPDigestAuth
    response = requests.get(url, auth=HTTPDigestAuth(username, password))
    return response.status_code, response.content

def digest_server(realm, env, get_hashed_password):
    #
    # Server side authentication function
    # env is WSGI evironment
    # get_password is a function: password = get_password(realm, username)
    # 

    def md5sum(data):
        from hashlib import md5
        m = md5()
        if isinstance(data, str):
            data = data.encode("utf-8")
        m.update(data)
        return m.hexdigest()

    auth_header = env.get("HTTP_AUTHORIZATION","")
    #print ("auth_header:", auth_header)
    matches = re.compile(r'Digest \s+ (.*)', re.I + re.X).match(auth_header)
    
    
    if not matches:
        # need "Authorization" header
        nonce = secrets.token_urlsafe()
        #nonce = base64.b64encode(str(int(time.time())).encode("utf-8"))
        header = 'Digest realm="%s", nonce="%s", algorithm=MD5, qop="auth"' % (realm, nonce)
        return False, header        
    
    
    vals = re.compile(r', \s*', re.I + re.X).split(matches.group(1))

    dict = {}

    pat = re.compile(r'(\S+?) \s* = \s* ("?) (.*) \\2', re.X)
    for val in vals:
        ms = pat.match(val)
        if ms:
            dict[ms.group(1)] = ms.group(3)

    user = dict['username']
    saved_digest = get_hashed_password(realm, user)        # as hex
    #print("saved digest:", saved_digest)
    if saved_digest == None:
        # unknown user
        return False, None


    #a1 = md5sum('%s:%s:%s' % (user, realm, cfg_password))        
    a2 = md5sum('%s:%s' % (env['REQUEST_METHOD'], dict["uri"]))
    myresp = md5sum('%s:%s:%s:%s:%s:%s' % (saved_digest, dict['nonce'], dict['nc'], dict['cnonce'], dict['qop'], a2))
    if myresp == dict['response']:
        # success
        return True, user
    else:
        # password did not match
	    #print "signature mismatch"
        return False, None
