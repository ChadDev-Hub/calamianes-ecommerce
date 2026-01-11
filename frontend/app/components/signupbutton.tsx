'use client'

import { useState } from "react"

interface showFromProps{
    showform: () => void
}
export default function SignUpButton({showform}:showFromProps) {
    const [disabled, setDisabled] = useState(false)
    const handleClick = () =>{
        showform()
        setDisabled(!disabled)
    }
    return (
        <button onClick={handleClick} className="btn btn-neutral rounded-full">
            Signup
        </button>
    )
    
}