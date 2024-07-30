#!/usr/bin/node
// read file
const fs=require('fs')
const value=process.argv[2]
fs.readFile(value,'utf8',(err,data)=>{
    if (err){
        console.error('Error:',err)
    }
    console.log(data)
})