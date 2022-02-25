import React, { useState } from 'react';
import "../components/Header.css";


const Note=(props)=>{

    const deleteNote=()=>{
        props.onDelete(props.id);
    };
    return(
    <>
    <div className='style'>
        <div className='note'>
            <h3>{props.title}</h3>
            <p>{props.content}</p>
            <button onClick={deleteNote}>Delete</button>
        </div>
    </div>
    </>
    );
}

export default Note;