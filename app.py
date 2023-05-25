from flask import Flask


FAI=Flask(__name__)

@FAI.route('/wish/<na>')
def wish(na):
    return f'Hye How are you {na}'


if __name__=='__main__':
    FAI.run(debug=True,host='192.168.100.242',port=5002)