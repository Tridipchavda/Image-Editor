import logo from './logo.svg';
import './App.css';
import Header from './components/Header.js';
import Form from './components/Form.js';
import Note from './components/Note.js';
import { useState } from 'react';

function App() {
  const [item,setItem]=useState([]);

  const AddNote=(note)=>{
    //alert('I am clicked');

    setItem((prev)=>{
    return [...prev,note]
    })
  }
  const Del=(id)=>{
    setItem((old)=>
      old.filter((currdata,index)=>{
        return index != id;
      })
    )
  }
  return (
    <div>
      <Header/>
      <Form  NoteBook={AddNote}/>
      

      {item.map((val,index)=>{
        return (<Note id={index} key={index} title={val.title} content={val.content} onDelete={Del}/>);
      })}
   </div>
  );

  
}

export default App;
