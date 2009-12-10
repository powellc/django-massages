=================
Django Massages
=================
:author: Colin Powell
:date: 2009-12-09
:copyright: One Cardinal

Overview
---------
This is a very simple django application for managing massages for a massage therapy website.

Views
------

* **mg-index** Provides a list of massages and, optionally, if any of the massages are listed as "standard rate," a price list. The price list is composed of all of it's rates, plus whatever other massages not listed as "standard rate" cost.

* **mg-detail** Currently unimplemented. Obviously this would provide details of a particular massage, though there is currently no extra data to show on this page, making it a bit silly to implement it.

Models
-------

* **Massage**

  - Title

  - Slug
 
  - Description

  - Image

  - Rate
  
  - At Rate?

* **Price List**

  - Title

  - Rates

  - Active?

* **Rate**

  - Time

  - Price

URLs
------
* /(index)