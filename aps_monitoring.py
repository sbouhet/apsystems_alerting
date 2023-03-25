import argparse
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import subprocess
import os

class ApsMonitoringManager:

    def action_check(self,notification):

        print("Start playwright test ...")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        process = subprocess.run([dir_path+"/run-docker.sh", os.environ['APSYSTEMS_USER'], os.environ['APSYSTEMS_PWD']], capture_output=True)
        output = process.stdout.decode("utf-8")

        if process.returncode == 0:
            if notification:
                self.send_notification('APS monitoring OK', output,'#00FF00')
        else:
            self.send_notification('APS monitoring FAILED', output,'#FF0000')

        return

    def send_notification(self,text_subject,text_body,color):

        url = 'https://www.pushsafer.com/api'
        post_fields = {
            "t": text_subject,
            "m": text_body,
            "i": 1,
            "c": color,
            "d": 'a',
            "u": 'https://www.apsema.com/ema/index.action',
            "ut": 'AP Systems',
            "k": os.environ['PUSHSAFER_KEY'],
        }

        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()

        print('Notification sent: '+json)

if __name__ == '__main__':

    parser = argparse.ArgumentParser("aps monitoring manager")
    parser.add_argument(
        '--action',
        default='check',
        action='store',
        choices=['check'],
        help='Define action'
    )

    parser.add_argument('--notification', action='store_true')
    parser.add_argument('--no-notification', dest='notification', action='store_false')
    parser.set_defaults(notification=True)

    args = parser.parse_args()

    print("Action:"+args.action)
    print("Notification:"+str(args.notification))

    t = ApsMonitoringManager()

    if args.action == 'check':
        t.action_check(args.notification)



