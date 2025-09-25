<div align="center">
   <h1>🖥️ StashHouse: SSH Plugin</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [🛡️ Security](#security)

</div>

<hr />

# Purpose

A plugin for [StashHouse](https://pypi.org/project/stashhouse/) to include a Secure Copy Protocol (SCP) and Secure File 
Transfer Protocol (SFTP) server without authentication.

Registers a plugin named `ssh` and provides a `--ssh.port` argument to configure the port to listen on.

# Security

By default, this plugin should **not** be deployed in an internet-facing manner to prevent unwanted file uploads. Always 
deploy it with appropriate security restrictions such as, but not exclusively, firewall rules.
