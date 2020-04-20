# AI_Automation

##### Code for setup.sh (Alternate with no credentials.toml)
```sh
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```


##### Code For Procfile
```sh
web: sh setup.sh && streamlit run app.py
```
