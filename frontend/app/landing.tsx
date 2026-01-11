'use client'

import Navbar from "./components/navbar";
import Image from "next/image";
import SignUpButton from "./components/signupbutton";
import LoaginButton from "./components/loginbutton";
import SignupForm from "./components/signupform";
import { useState } from "react";
interface HomeClientProps{
    data: {
    description:string,
    title:string
}
}
export default function Landing({data}:HomeClientProps){
    const [showForm, setShowForm] = useState(false)
    const handleShowForm = () => {
        setShowForm(!showForm)
    }
    const handleCloseForm = () =>{
        setShowForm(false)
    }
    return(
        <div>
            <Navbar title={"Welcome to Calamian Ecommerce"}/>
        <div className="pt-40 p-4 bg-linear-to-t from-white-500 to-gray-400">
          <div className="grid lg:grid-cols-2 sm:grid-cols-1 mx-5 lg:mx-50  gap-20">
              <div className="flex flex-col antialiased font-bold gap-10">
                  <h1 className="text-4xl text-center md:text-left">{data.title}</h1>
                  <p className="text-base/7">{data.description}</p>
                  <div className="flex justify-end gap-2">
                      <SignUpButton showform={handleShowForm}/>
                      <LoaginButton/>
                  </div>
              </div>
              <div className="relative rounded-full" >
                <Image
                loading="eager"
                src="/Computer Icon.png"
                alt="icon"
                width={900}
                height={300}
                className="rounded-full"/>
              </div>
          </div>
        </div>
        {showForm && <SignupForm closeform={handleCloseForm}/>}
        </div>
        
    )
}