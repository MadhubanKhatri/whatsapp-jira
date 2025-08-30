import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Dashboard.css';
import Home from './Home.jsx'

function Dashboard() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedTicket, setSelectedTicket] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/fetch_drafts')
      .then(response => {
        setTickets(response.data['draft_tickets']);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const handleSetDetails = (ticket) => {
    console.log("TiCKet: ",ticket);
    
    setSelectedTicket({
      id: ticket.id,
      title: ticket.title,
      description: ticket.description,
      priority: ticket.priority_id,
      labels: ticket.labels
    });
  };

  return (
    <div className="dashboard-bg">
      <h2 className="dashboard-title">Unapproved Jira Tickets</h2>
      {loading ? (
        <div className="dashboard-loading">Loading...</div>
      ) : (
        <div className="dashboard-table-wrapper">
          {tickets && tickets.length === 0 ? (
            <div className="dashboard-empty">No unapproved tickets.</div>
          ) : (
            <table className="dashboard-table">
              <thead>
                <tr>
                  <th>Title</th>
                  <th>Description</th>
                  <th>Priority</th>
                  <th>Labels</th>
                </tr>
              </thead>
              <tbody>
                {tickets && tickets.map((ticket, idx) => (
                  <tr key={idx}>
                    <td
                      onClick={() => handleSetDetails(ticket)}
                      style={{ color: "#4f8cff", cursor: "pointer" }}
                    >
                      <b>{ticket.title}</b>
                    </td>
                    <td>{ticket.description}</td>
                    <td>
                      <span className={`priority-badge priority-${ticket.priority_id?.toLowerCase()}`}>
                        {ticket.priority_id}
                      </span>
                    </td>
                    <td>
                      <div className="labels-section">
                        {ticket.labels && ticket.labels.map((label, i) => (
                          <span className="label-badge" key={i}>{label}</span>
                        ))}
                      </div>
                    </td>


                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}

        {
            selectedTicket && (<Home
                                    id={selectedTicket?.id}
                                    title={selectedTicket?.title}
                                    description={selectedTicket?.description}
                                    priority={selectedTicket?.priority}
                                    labels={selectedTicket?.labels}
                                />
        )
        }
      
    </div>
  );
}

export default Dashboard;
