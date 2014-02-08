StackExchangeElasticSearch
==========================

Playing with ElasticSearch and the SciFi Stackexchange Dataset

Requires Python & Virtualenv, to setup:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
      
      
Index docs to stackexchange:

    python postToEs.py posts.xml
    
    
Play around with MySQL's FT features (requires MySQL) with the "whysearch" ipython notebook. Be sure to update the sample store.py with your valid MySQL credentials.
      
  
