import { useEffect,useState } from 'react'

 import {SlLike ,SlDislike} from 'react-icons/sl'
import './App.css'
import axios from 'axios'

function App() {
  
  const [data,setData] = useState([])
  let {id,likes,dislikes} = data
  
  
  useEffect(()=>{
    
    fetchData()
  },[])
  console.log(data)

  const fetchData = async() =>{
      
    const res  = await axios.get('http://localhost:8000/votes')
    const data = res.data 

    
    data.map((item)=> setData(item))
  }

  const handleLikes = async () => {
    likes = likes + 1
    const data ={
      likes:likes,
      dislikes:dislikes
    }
    await axios.put(`http://localhost:8000/vote/${id}`,data)
    fetchData()

  }

  const handleDisLike = async () => {
    dislikes = dislikes + 1
    const data ={
      dislikes:dislikes,
      likes : likes
    }
    await axios.put(`http://localhost:8000/vote/${id}`,data)
    fetchData()

  }
  
 

  return (
    <div className="App">
      
      <div className="likes">
        <div className="item">
         <button className='dis' onClick={handleDisLike}>Dislike <SlDislike /></button>
         <h4>{dislikes}</h4>
        </div>
       <div className="item">
          <button className='add' onClick={handleLikes}>Like <SlLike /></button>
          <h4>{likes}</h4>
       </div>
      
      </div>
      
      
    </div>
  )
}

export default App
