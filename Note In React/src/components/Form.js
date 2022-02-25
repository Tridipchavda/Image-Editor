import React, { useState } from 'react';
import "../components/Header.css";


const Form=(props)=>{
    
    const [note,setNote]=useState({        
        title:"",
        content:"",
    });
    
    const SeeData=(event)=>{
      
        const {name,value}=event.target;
        setNote((prev)=>{
            return {
                ...prev,
                [name]: value,
            };   
        });
        console.log(note);
    }

    const AddEvent=()=>{
        props.NoteBook(note)
    }

    return(
    <>
        <div className='main'>
        
            <input className='title' value={note.title} onChange={SeeData} name='title' type='text'  placeholder='Title'></input>
            <textarea className='extra' value={note.content} onChange={SeeData} name='content' type='text' placeholder='Enter details here' rows='' cols='' />
            <button className='btn' onClick={AddEvent}>+</button>
      
        </div>
    </>
    );
}

export default Form;