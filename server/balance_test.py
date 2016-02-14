import messagebird

TEST_KEY = '<INSERT_TEST_KEY_HERE>'
LIVE_KEY = '<INSERT_LIVE_KEY_HERE>'

KEY = LIVE_KEY

nummer = '<INSERT_NUMBER_HERE>'

def send_voice_message(number, message):
    try:
        client = messagebird.Client(KEY)
        vmsg = client.voice_message_create(number, message, { 'reference' : 'coole game' })
        print "Sent voice to %s: %s" % (number, message)
        balance = client.balance()
        print "We have", balance.amount, "messages left."

        return vmsg
    except Exception as e:
        print e
        return
        for error in e.errors:
            print "Error:", error.description

def send_text_message(number, message):
    try:
        client = messagebird.Client(KEY)
        vmsg = client.message_create("FromGame", number, message, { 'reference' : 'coole game' })
        print "Sent text to %s: %s" % (number, message)
        balance = client.balance()
        print "We have", balance.amount, "messages left."

        return vmsg
    except Exception as e:
        print e
        return
        for error in e.errors:
            print "Error:", error.description


if __name__ == "__main__":
    try:
        client = messagebird.Client(KEY)
    
        balance = client.balance()
        print "We have", balance.amount, "messages left."
        
        vmsg = client.voice_message_create(nummer, 'Hello Tim, while you where sleeping a bomb has been set off. Go upstairs to defuse it right now.', { 'reference' : 'coole game' })

        print('\nThe following information was returned as a VoiceMessage object:\n')
        print('  id                : %s' % vmsg.id)
        print('  href              : %s' % vmsg.href)
        print('  originator        : %s' % vmsg.originator)
        print('  body              : %s' % vmsg.body)
        print('  reference         : %s' % vmsg.reference)
        print('  language          : %s' % vmsg.language)
        print('  voice             : %s' % vmsg.voice)
        print('  repeat            : %s' % vmsg.repeat)
        print('  ifMachine         : %s' % vmsg.ifMachine)
        print('  scheduledDatetime : %s' % vmsg.scheduledDatetime)
        print('  createdDatetime   : %s' % vmsg.createdDatetime)
        print('  recipients        : %s\n' % vmsg.recipients)

    except messagebird.client.ErrorException as e:
        print('\nAn error occured while requesting a VoiceMessage object:\n')

        for error in e.errors:
            print('  code        : %d' % error.code)
            print('  description : %s' % error.description)
            print('  parameter   : %s\n' % error.parameter)
