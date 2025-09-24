"""
The `certbot_dns_abion.dns_abion` plugin automates the process of completing a ``dns-01`` challenge
by creating, and subsequently removing, TXT records using the Abion DNS API.

Named Arguments
---------------
========================================  =====================================
``--dns-abion-credentials``              Path to Abion credentials INI file. (Required)
``--dns-abion-propagation-seconds``      Number of seconds to wait for DNS propagation
                                        before asking the ACME server to verify the DNS record.
                                        (Default: 60)
========================================  =====================================

Credentials
-----------
Use of this plugin requires a configuration file containing an Abion API key,
obtained from your Abion account dashboard. The file should look like:

.. code-block:: ini

   dns_abion_api_key = YOUR_ABION_API_KEY
   dns_abion_api_url = https://api.abion.com/        # optional, default URL
   dns_abion_dns_ttl = 60                             # optional, default TTL

The path to this file can be provided using the ``--dns-abion-credentials`` command-line argument.
Certbot records the path to this file for renewal.

Security Note
-------------
You should protect this credentials file as you would protect any sensitive secret.
Users who can read this file or run Certbot with these credentials may
be able to create or revoke certificates for domains under your control.

Example
-------

To acquire a certificate for ``example.com``:

.. code-block:: bash

   certbot certonly \\
     --dns-abion \\
     --dns-abion-credentials ~/.secrets/abion.ini \\
     -d example.com

To acquire a certificate for ``example.com`` and ``*.example.com``:

.. code-block:: bash

   certbot certonly \\
     --dns-abion \\
     --dns-abion-credentials ~/.secrets/abion.ini \\
     -d example.com \\
     -d '*.example.com'

"""
