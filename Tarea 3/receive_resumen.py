import pika, sys, os

import wikipedia

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()


    channel.queue_declare(queue='resumen')


    def callback(ch, method, properties, body):

        wikipedia.set_lang("es")
        resumen = wikipedia.summary(body, auto_suggest=False)

        print(" [x] Resumen: %r" % resumen)

    channel.basic_consume(queue='resumen', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

