import json
from flask import Flask, render_template, request, Response
from netmiko.ssh_exception import NetMikoAuthenticationException
from napalm.base.exceptions import ConnectionException
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

from helper import read_yaml, napalm_get_facts, rest_native_interface, convert_interface_data

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    devices = read_yaml('devices.yaml')
    return render_template('index.html', routers=devices)


@app.route('/interface_status/<router>')
def status(router):
    try:
        interfaces = rest_native_interface(router)
        app.logger.debug('interface data (%s): %s ', router, interfaces)
        return render_template('status.html', router=router, interfaces=convert_interface_data(interfaces))
    except ConnectionError:
        return Response(response=f'Connection to {router} not possible', status=408)
    except HTTPError as e:
        return Response(response=f'HTTP Error: {e}', status=e.response.status_code)

@app.route('/show_facts/<router>')
def show_facts(router):
    try:
        facts = napalm_get_facts(router)
        app.logger.debug('device facts (%s): %s ', router, facts)
        text = json.dumps(facts, indent=2)
        return render_template('show_facts.html', router=router, facts=text)
    except NetMikoAuthenticationException:
        return Response(response='Authentication failed. Check your cisco user/password', status=401)
    except ConnectionException:
        return Response(response=f'Connection to {router} not possible.', status=408)


if __name__ == '__main__':
    app.run(debug=True)
