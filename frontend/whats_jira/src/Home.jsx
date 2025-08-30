import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './Home.css'

function Home(props) {
    const [id, setId] = useState('');
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [priority, setPriority] = useState('');
    const [labels, setLabels] = useState([]);

    const [isEditing, setIsEditing] = useState(false);
    const [isTitleEditing, setIsTitleEditing] = useState(false);
    const [isDescEditing, setIsDescEditing] = useState(false);

    // Update state when props change
    useEffect(() => {
        console.log("PROPS: ",props);

        if (props.id !== undefined) setId(props.id);
        if (props.title !== undefined) setTitle(props.title);
        if (props.description !== undefined) setDescription(props.description);
        if (props.priority !== undefined) setPriority(props.priority);
        if (props.labels !== undefined) setLabels(props.labels);
    }, [props.title, props.description, props.priority, props.labels]);

    const handleTextClick = (target) => {
        if (target == "title"){
            setIsTitleEditing(true);
            setIsDescEditing(false);
        }else{
            setIsDescEditing(true);
            setIsTitleEditing(false);
        }
        setIsEditing(true);
    }
    const handleUpdate = () => {
        setIsEditing(false);
        setIsDescEditing(false);
        setIsTitleEditing(false);
    }
    const handleApprove = () => {
        const data = {
            'id': id,
            'title': title,
            'description': description,
            'priority': priority,
            'labels': labels
        }
        axios.post('http://127.0.0.1:8000/jira_ticket', data)
            .then(response => {
                console.log("DATAAAAA: ",data);
                
                console.log("jira ticket created");
            }
            )
    }

  return (
    <div className="home-bg">
      <div className="card-container">
        <div className="card-header">
          {isTitleEditing 
            ? <input 
                className="title-input"
                type="text" 
                value={title} 
                onChange={(e)=>setTitle(e.target.value)}
                placeholder="Title"
              /> 
            : <h1 className="title" onClick={()=>handleTextClick("title")}>{title}</h1>
          }
        </div>
        <div className="card-body">
          <div className="desc-section">
            <label className="desc-label">Description:</label>
            {isDescEditing 
              ? <textarea 
                  className="desc-input"
                  value={description}
                  onChange={(e)=>setDescription(e.target.value)}
                  placeholder="Description"
                /> 
              : <p className="desc-text" onClick={()=>handleTextClick("desc")}>{description}</p>
            }
          </div>
          <div className="meta-section">
            <span className={`priority-badge priority-${priority?.toLowerCase()}`}>{priority}</span>
            <br/>
            <div className="labels-section">
              {labels && labels.map((item, idx) => (
                <span className="label-badge" key={idx}>{item}</span>
              ))}
            </div>
          </div>
        </div>
        <div className="card-footer">
          {!isEditing ? (<button className="approve-btn" onClick={handleApprove}>Approve</button>) : (
            <>
            <button className="update-btn" onClick={handleUpdate}>Update</button>
            <button className="cancel-btn" onClick={handleUpdate}>Cancel</button>
            </>
          )}
        </div>
      </div>
    </div>
  )
}


export default Home;
