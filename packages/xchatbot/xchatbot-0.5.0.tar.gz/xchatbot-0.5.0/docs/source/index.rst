.. XChatBot documentation master file, created by
   sphinx-quickstart on Sun Apr 26 12:46:31 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The Xtensible XMPP Chat Bot
====================================

``XChatBot`` is a xmpp bot library written in python using the 
`nbxmpp library from Gajim <https://dev.gajim.org/gajim/python-nbxmpp/>`_

.. contents:: :local:

Requirements
------------

- python 3
- pygobject
- nbxmpp

optionally

- pipenv

Install
-------

With ``pip``
''''''''''''

.. code-block:: none

    pip install xchatbot


Using ``git``
'''''''''''''

.. code-block:: none

    git clone https://git.sr.ht/~fabrixxm/xchatbot


then install required packages:

**with pipenv**::

    pipenv --site-packages --python 3
    pipenv install

**on osx** you need first to install python3 with brew::

    brew install python3 pipenv pygobject3 libsoup

**on Arch**::

    pacman -S python-gobject python-nbxmpp

**on Debian**::

    apt install python3-gi python3-nbxmpp



Configuration
-------------

Config for the bot is passed in an instance of :class:`xchatbot.Config`.

The class method :func:`xchatbot.Config.load` will load a configuration 
file by name, looking for ``./<filename>.rc``, ``~/.<filename>.rc`` and 
``/etc/<filename>.rc`` in this order, and will load the first it finds.

An example config file is provided as `echobot.rc.dist`, with comments.

See :doc:`xchatbot.rc`


Customize the bot
-----------------

Subclass :class:`xchatbot.XChatBot` class and implement your commands as 
method of your class.

A bot class can have public commands and private commands. Is it also possibile 
to define a default to handle unknown commands.

The bot is started calling the classmethod :func:`~xchatbot.XChatBot.start`

Commands
--------

The bot will react to specific commands with optionals arguments.

Commands are method of the class named ``cmd_commandname``.
Each command method must get a ``peer`` (:class:`~xchatbot.Peer`) parameter 
and optionally a number of args.

A docstring should be provided that is used by ``help`` command to build the 
help message.

If the numbers of args given in the message doesn't match the function 
signature, an error message is returned.

By convention, command arguments are listed before description in method 
docstring


Here an example:

.. code-block:: python

	from xchatbot import Config, XChatBot, Peer

	# My custom bot
	class MyEchoBot(XChatBot):
	
		# 'hello' command. Takes no arguments
		def cmd_hello(self, peer:Peer):
			"""Say hello to the bot"""
			peer.send("Hello to you!")
	
		# 'sum' command. Takes exactly two arguments
		def cmd_sum(self, peer:Peer, a:str, b:str):
			"""<a number> <another number> - Sum two numbers"""
			peer.send(str(int(a) + int(b)))
	
		# 'echo' command. Takes a variable number of arguments
		def cmd_echo(self, peer:Peer, *args):
			"""Echo back what you typed"""
			msg = "You said: " + " ".join(args)
			peer.send(msg)

	if __name__ == "__main__":
		config = Config.load("myechoboot")
		MyEchoBot.start(config)


To test this, create a ``myechobot.rc`` config file and run the bot::

    $ python myechobot.py


Private commands
----------------

A command can be marked as private using the ``@private`` decorator.

A private command is listed in help and is executed only if the message comes
from the admin JID set in config file

.. code-block:: python

	from xchatbot import XChatBot, Peer, private

	class MyEchoBot(XChatBot):
		...
		
		# a private command. Takes a single argument
		@private
		dev cmd_lights(self, peer:Peer, status):
		    """<status:on or off> - Turn lights on or off"""
		    if status == "on":
		        # turn on the lights
		        peer.send("Lights are now on")
		    elif status == "off":
		        # turn off the lights
		        peer.send("Lights are now off")
		    else:
		        peer.send("please, 'on' or 'off'.")



Default command
---------------

If no commands match the message received, `default()` method is called.
Your bot class can override this method to return a default response:

.. code-block:: python

	class MyEchoBot(XChatBot):
		...
		def default(self, peer, *args):
		    peer.send("I'm sorry, I don't understand you. Write me 'help'")



Logging
-------

A pre-configured `logging.Logger` object is available as class attribute `logger`

.. code-block:: python

	class MyEchoBot(XChatBot):
		...
		def cmd_log(self, 



Modules
=======
.. toctree::
   :maxdepth: 4
   :caption: Contents:

   xchatbot
   xchatbot.rc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
