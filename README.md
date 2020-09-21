# ASA VPN monitoring with ThousandEyes

In 2020 providing remote access to users and building out a solid VPN infrastructure has become absolutely mission critical. The challenge for IT organisations is how do they look to provide better monitoring and assurance of these infrastructures, particuarly when users are accessing from networks and devices which the organisation may not actually own or be able to manage.

In order to help with this, we've [previously looked at VPN utilisation monitoring](https://github.com/sttrayno/ASA-Telemetry-Guide) using off the shelf tools such as pyATS and the TIG stack. This was popular at the time so I thought it might be time to build on this a little more.

In this guide, we're going to attempt to expand on this more, by looking to encorporate the ThousandEyes platform in order to monitor the availability of ASA's further for checking access of other metrics such as availability and packet loss to the ASA over the internet. For those who aren't familiar with ThousandEyes, ThousandEyes was aquired by Cisco in August 2020 - it specialises in monitoring the avialability and performance across networks which you don't own or manage, such as public clouds or the internet. ThousandEyes is an extremely powerful platform for being able to not only understand when faults are happening but also pinpoint exactly where in the network and what's going wrong. Take for example an outage in a specific ISP or a network issue in a specific region within the public cloud, it's these exact issues which ThousandEyes looks to be able to provide more situational awareness for.

The products and techniques used in this guide are suitable and avialable in a way that can be used for companies of all sizes aslong as you have an ASA and ThousandEyes. It should also be said that this should be possible with other remote access VPN solutions also as long as ThousandEyes has support to build a test for it (HTTP in this case) you shouldn't have too much of an issue using the monitoring techniques discussed in this guide.

### Prerequsite #1 - ThousandEyes account

Fortunately, as it stands you can register for a 15 day trial of ThousandEyes if you'd like to get started. To do this go to the [ThousandEyes site](https://www.thousandeyes.com) and click on the "request free trial button". Once you register and provide the required details you should then be taken to the ThousandEyes dashboard.

### Prerequsite #2 - An ASA with remote access configured

Of course, as we are monitoring an ASA we'll need one of these configured and ready to provide remote access, now I'm not going to go into this level of detail within this guide. However here's some resources which may help you get up and running if you aren't already:

* ASA 9.0 Configuration guide - https://www.cisco.com/c/en/us/td/docs/security/asa/asa90/configuration/guide/asa_90_cli_config/vpn_remote_access.html
* Step-by-step guide on configuring Remote access VPN on ASA - https://networklessons.com/cisco/asa-firewall/cisco-asa-remote-access-vpn
* An Ansible playbook built to automate ASA remote access deployment - https://github.com/sttrayno/ASAonAWS-Ansible-Deployment

### Building a ThousandEyes test

The first thing we have to do in ThousandEyes is to create a test to look to monitor our ASA device, when you login to ThousandEyes you should be directed to the main dashboard, from here you can configure your tests you wish to run. To do this navigate to "test settings" under "Cloud and Enterprise Agents" and select "Add New Test" a menu should then pop up allowing you to customise the different kind of test's you can run. For now we're going to stick with the default "HTTP Server"

Give your test a name and where it asks for a URL specify the IP address of your ASA (This can be a FQDN or an IP address, if you provide a FQDN an extra level of DNS testing data will be provided).

![](./images/create-test.gif)

You'll see an option for the agents you wish to run this test on, select a few agents here, I'd recommend choosing one from each region. These agents are the default cloud agents which are available in the ThousandEyes trial, to learn more head down to the "Types of test" section to read into the different types of test that are available.

Note: At the time of writing within the TE trial period, there are 29 agents available you can only run a single test on each Agent.

You will also see an option to select the alerts you recieve, for now I'd leave this at the default

![](./images/select-agents.gif)

When you're done, select "Create New Test" and it should be created within a few seconds, select on the test you've just created and you should see a button for "Run Once" select that and give TE a few minutes to run its tests. It should return an example view as we've got below.

![](./images/run-test.gif)

Congratulations, you've just created your first test in ThousandEyes, take some time to explore the types of tests and the advanced settings to get a feel for how you could customise the testing scenarios for your exact environment.

![](./images/run-test-cont.gif)

### Disabling SSL validation (Optional)

In this example, as I don't have a valid certificate on my ASA. Therefore when my tests run I get an availability fail as the certifcate is invalid, to get round this I can disable SSL validation under the advanced settings by unchecking "Verify SSL certificate"

![](./images/disable-ssl.gif)

### Types of test

In the ThousandEye platform there are different types of agents which we can run tests on, each of these have different advantages and considerations which will dictate what you use. A quick explanation of the most popular tests:

* Cloud Agents - These are the agents in which we ran our test in the first section of the guide, cloud agents are managed and maintained by ThousandEyes across nearly [200 cities globally](https://www.thousandeyes.com/product/cloud-agents) which allow you to test availablility and performance from multiple different geos, clouds and ISP's. In the free trial there are 29 different agents available to run tests on

* Enterprise Agents - These are agents you deploy on your own infrastructure, this is by far the most flexible method of deployment and there's many options for installing the agent including OVA, Docker container and installable package. You will have to manage these agents yourself as an adminstrator however they give great flexibility in terms of being able to run pretty much anywhere you require.

* Endpoint Agents - These are deployed on the end-users actual device, this can be installed on a browser (Edge, Chrome or Firefox) or on the OS (MacOS or Windows). These provide a major advantage of being able to track the users actual experiences, across multiple devices, ISPs and physical locations. The drawback being is you have to manage the install of the agents to user machines, which in large environments can be tricky.

You can decide if any of the agents outlined above may suit your environment better, it might be possible for you to distribute the endpoint agent to user machines which will provide a more respresentative view of user experience. However this will add a level of complexity so it's a trade-off

### Visualisation and Alerts

Within the stock ThousandEyes platform there is the dashboard screen, from here you can build custom views to check on the status of your tests and build out charts to allow you to track the key metrics you need. Such as the examples below: 

![](./images/dashboards.gif)

There are some limitations with the visualisation as you'll typically have a limit of 30 days which means long term visualisations can be an issue. We'll go onto address this in the next section.

Within ThousandEyes when you run your tests you can also set the alerts that you wish to be notified when a test 'fails' by default this will send an email to you however you can tweak based on your exact needs. 

### Advanced visualisations with Grafana

In the case that the stock alerting and visualisation in the ThousandEyes platform isn't enough for you or you need to have a more historical view of information over 30 days, we can also use open source tools such as Grafana, part of the TIG stack to build more custom visualisations. As the data in ThousandEyes is all available through a REST API it's a fairly straight forward process.

From here you could now look to follow our [previous](https://github.com/sttrayno/ASA-Telemetry-Guide) to look at getting device metrics in conjunction with these availability and performance numbers.

### Appendix - Endpoint agent monitoring

As mentioned earlier,
