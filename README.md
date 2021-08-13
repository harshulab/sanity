
# Sanitizer Backend


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MAIL_USERNAME`
`MAIL_PASSWORD`
`RECIPIENTS`
## Deployment

To deploy this project run

```bash
Add your mail id, mail password and recipients in /etc/environment file as
```

```bash
export MAIL_USERNAME="your id"
```
```bash
export MAIL_PASSWORD="your pass"
```

  
```bash
export RECIPIENTS="the id of the reciver"
```


Run this command in pythonFile directory 


```bash
 sudo apt-get install docker 
```

```bash
sudo apt-get install docker-compose 
```

```bash
sudo docker-compose -f docker-compose.yml up --build -d
```


  
## Authors

- [@avnoor-488](https://www.github.com/avnoor-488)

  
