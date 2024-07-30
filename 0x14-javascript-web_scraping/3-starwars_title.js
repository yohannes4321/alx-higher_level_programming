#!/usr/bin/node
 

value1=process.argv[2];
url='https://swapi-api.alx-tools.com/api/films/'
const request=require('request')
const url_final=url+value1
request(url_final,(err,response,body)=>{
    if (err){
        console.err(err)

    }
     
    console.log(JSON.parse(body).title)

});