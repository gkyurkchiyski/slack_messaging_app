import requests
import sys
import getopt

# Send Slack Message Using Slack API

def send_slack_message(message):
    payload = '{"text":"%s"}' % message 
    response = requests.post('https://hooks.slack.com/services/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',
                             data=payload)
    print(response.text)
    
 def main(argv):
    
    message = ' '
    
    try: opts, args = getopt.getopt(argv, "hm:", ["message="])
    
    except getopt.GetoptError:
        print('SlackMessage.py -m <message>')
        sys.exut(2)
    if len(opts) == 0:
        message = "Test success!"
    for opt, arg i opts:
        if opt == '-h':
            print('SlackMessage.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
            
    send_slack_message(message)          
    
if __name__ == "__main__":
    main(sys.argv[1:])  
