# Service for collecting data

Building a full-fledged service site that collects data on vacancies from job search sites and sends them to subscribers. Service subscribers are registered by choosing a city and programming language. Once a day, all subscribers who want to receive emails with vacancies are selected and based on their preferences, a list of URLs is formed, by which parsers are launched to collect vacancies by these parameters. After the parsers are finished, the sending of letters to those who want to receive the newsletter starts.

## Link to the deployed project

[Site](https://scraping-j.herokuapp.com/)