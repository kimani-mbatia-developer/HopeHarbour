import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"

function AdminPageDashboard(){

    const navigate = useNavigate()

    const [charityApplications,setCharityApplications]=useState([])
    const [evaluatedApplications, setEvaluatedApplications]=useState([])

    useEffect(()=>{
        fetch('https://hopeharbour-api.onrender.com/admin/applications/pending')
        .then((response)=>response.json())
        .then(response=>{
            setCharityApplications(response.data)
        })
        .catch(error =>{alert(error)})
    },[])

    const dashboardContainer1={
        //position:"relative",
        marginTop:"3%",
        backgroundColor:"#569DDF",
        width:"1250px",
        height:"300px",
        borderRadius:"30px"
    }

    const dashboardContainer1Text={
        fontFamily:"HeeboBold",
        color:"white",
        paddingTop:"3%",
        paddingLeft:"5%"
    }

    const dashboardContainer2Heading={
        fontFamily:"HeeboBold",
        color:"black",
        paddingTop:"3%",
        paddingLeft:"5%",

    }

    const charityContainer={
        //textAlign:"center",
        position:"relative",
        //top:"1%",
        backgroundColor:"#E9E9E9",
        width:"90%",
        borderRadius:"30px",
        marginTop:"1%"
    }

    const charityContainer2={
        position:'relative',
        display:"flex",
        //top:"10%",
        backgroundColor:"#569DDF",
        //width:"90%",
        height:"150px",
        borderRadius:"30px",
        marginTop:"1%",
        marginBottom:"1%",
    }

    const SupportButton={
        border:"none",
        backgroundColor:"#77C5D6",
        borderRadius:"30px",
        height:"5%",
        width:"15%",
        color:"white",
        fontFamily:"HeeboBold",
        marginTop:"2%",
        marginLeft:"40%"

    }

    const approveButtonStyle={
        border:"solid white 1px",
        backgroundColor:"#77C5D6",
        borderRadius:"30px",
        color:"white",
        height:"30%",
        width:"90%",
        marginTop:"4%",
        marginLeft:"5%"
    }
    const rejectButtonStyle={
        border:"solid white 1px",
        backgroundColor:"red",
        borderRadius:"30px",
        color:"white",
        height:"30%",
        width:"90%",
        marginTop:"4%",
        marginLeft:"5%"
    }

    const closedButtonStyle={
        textAlign:'center',
        border:"none",
        //backgroundColor:"red",
        borderRadius:"30px",
        color:"white",
        height:"30%",
        width:"30%",
        margin:"10%"
    }

    function approveApplication(event){
        //event.preventDefault()
        //alert(event.target.id)
        const selectedCharityId= event.target.id
        fetch(`https://hopeharbour-api.onrender.com/admin/applications/approve/${selectedCharityId}`,{
            method:"PUT",
            headers:{
                    'Content-Type':'application/json'
            },
            body:JSON.stringify({
                application_id : selectedCharityId
            }),
        })
        .then(res=> alert(res.message))
        .catch(err=>{
            alert(err)
        })
        
    }


    function rejectApplication(event){
        //event.preventDefault()
        //alert(event.target.id)
        const selectedCharityId= event.target.id
        fetch(`https://hopeharbour-api.onrender.com/admin/applications/reject/${selectedCharityId}`,{
            method:"PUT",
            headers:{
                    'Content-Type':'application/json'
            },
            body:JSON.stringify({
                application_id : selectedCharityId
            }),
        })
        .then(res=> alert(res.message))
        .catch(err=>{
            alert(err)
        })
        
    }


    function CharityApps(){
        let items = charityApplications.map((application)=>(
            <div className='container' id={application.id} style={charityContainer2}>
                <div className="row" style={{width:"100%",paddingTop:"50px"}}>
                    <div className="col-sm">
                        <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"15px", margin:"5%"}}>Application ID: {application.id}</h3>
                    </div>
                    <div className="col-sm">
                        <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"15px", margin:"5%"}}>{application.charity_name}</h3>
                    </div>
                    <div className="col-sm">
                        <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"15px", marginTop:"5%"}}>Status: {application.status}</h3>
                    </div>
                    <div className="col-sm">
                        <button id={application.id} style={approveButtonStyle} onClick={approveApplication} >Approve</button>
                    </div>
                    <div className="col-sm">
                        <button style={rejectButtonStyle} onClick={rejectApplication}>Reject</button>
                    </div>
                </div>
                
                
                
                {application.status=="Pending"?(<>
                   
                    
                </>
        
                                             ):(<p style={closedButtonStyle}>Closed</p>)}     
            </div>
                ))
        return items        
    }


    return(
        <div className="container" style={{height:"2500px"}}>
            <div className="container" style={dashboardContainer1}>
                <div className="row">
                    <div className="col" style={dashboardContainer1Text}>
                        <p style={{fontSize:"20px",fontFamily:"HeeboRegular", marginTop:"5%"}}>October 25 2023</p>
                        <h5 style={{ fontSize:"32px", marginTop:"5%"}}>Administrator Page (Restricted Access)</h5>
                        <p style={{fontFamily:"HeeboRegular", marginTop:"5%"}}>Stay updated on your the latest Applications</p>
                    </div>
                    <div className="col" style={{paddingTop:"1%"}}>
                    </div>
                </div>
            </div>
            <h3 style={dashboardContainer2Heading}>Recent donations to your Charity</h3>
                <div className="container" style={charityContainer}>
                        
                </div>
                <CharityApps/>
        </div>    
    )
}

export default AdminPageDashboard

