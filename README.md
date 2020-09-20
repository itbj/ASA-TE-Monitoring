# ASA VPN monitoring with ThousandEyes

In 2020 providing remote access to users and building out a good VPN infrastructure has become absolutely mission critical.

In order to help with this, we've [previously looked at VPN utilisation monitoring](https://github.com/sttrayno/ASA-Telemetry-Guide) using off the shelf tools such as pyATS and TIG stack. This was extremely popular at the time so I thought it might be time to build on this a little more.

In this guide, we're going to attempt to expand on this more, by looking to encorporate ThousandEyes monitoring in order to monitor the availability of ASA's further for checking access of other metrics such as availability and packet loss to the ASA. For those who aren't familiar with ThousandEyes, ThousandEyes is a company Cisco aquired in August 2020 - it specialises in monitoring the avialability and performance across networks which you don't own, such as public clouds or the internet. ThousandEyes is an extremely powerful platform for being able to not only understand when faults are happening but also pinpoint exactly where in the network and what's going wrong. Take for example an outage in a specific ISP or a network issue in a specific region within the public cloud, it's these exact issues which ThousandEyes looks to be able to provide more situational awareness on.

The products and techniques used in this guide are suitable and avialable in a way that means can be used for companies of all sizes aslong as you have an ASA and ThousandEyes. It should also be said that this should be possible with other remote access VPN solutions also as long as ThousandEyes has support to build a test for it (HTTP in this case) you shouldn't have too much of an issue using the monitoring techniques discussed in this guide.

### Prerequsite #1 - ThousandEyes account

Fortunately, as it stands you can register for a 15 day trial of ThousandEyes if you'd like to get started. To do this go to the [ThousandEyes site](https://www.thousandeyes.com) and click on the "request free trial button". Once you register and provide the required details you should then be taken to the ThousandEyes dashboard.

### Prerequsite #2 - An ASA

Ofcourse, as we are monitoring an ASA we'll need one of these configured and ready to provide remote access, now I'm not going to go into this level of detail within this guide. However here's some resources which ma

### Building a ThousandEyes test

#### Disable SSL validation (optional)

In this example, as I don't have a valid certificate on my ASA. I'm going to choose

### Types of test


