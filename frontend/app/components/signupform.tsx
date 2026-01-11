'use client'

import { useState } from "react"
interface closeFormProps{
    closeform: () => void
}
export default function SignupForm({closeform}:closeFormProps) {
    const API_BASE = process.env.NEXT_PUBLIC_API_ROUTER;
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [userName, setUserName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const submit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        const data = new FormData()
        data.append('firstname', firstName)
        data.append('lastname', lastName)
        data.append('username', userName)
        data.append('email', email)
        data.append('password', password)

        try {
            const res = fetch(`${API_BASE}/auth/signup`,
                {
                    method: "post",
                    body: data
                }
            );
            const result = await (await res).json()
            if (!(await res).ok) {
                console.log("error", (await res).status, result.detail)
                
            }
            else {
                console.log("Sucessull", data)
                closeform()
            }

        } catch (error) {
            console.log(error)
        }

    }
    return (
        <fieldset className="fieldset fixed top-1/4 left-1/2 -translate-x-1/2 bg-base-200 p-4 min-w-xs rounded-90">
            <legend className="fieldset-legend flex justify-between w-full">
                <div>
                    <h1 className="text-lg text-center  ">Signup Form</h1>
                </div>

                <div onClick={closeform} className="border self-end  rounded-full">
                    <div role="button" className="btn btn-circle btn-ghost btn-xs text-inf">
                        x
                    </div>
                </div>
            </legend>

            <form onSubmit={submit} >

                <div className="flex flex-col gap-4">


                    <div>
                        <input value={firstName} onChange={(e) => setFirstName(e.target.value)} required type="text" placeholder="First Name" className="input" />
                    </div>
                    <div>
                        <input value={lastName} onChange={(e) => setLastName(e.target.value)} required type="text" placeholder="Last Name" className="input" />
                    </div>
                    <div>
                        <label className="input validator">
                            <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                <g
                                    strokeLinejoin="round"
                                    strokeLinecap="round"
                                    strokeWidth="2.5"
                                    fill="none"
                                    stroke="currentColor"
                                >
                                    <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="12" cy="7" r="4"></circle>
                                </g>
                            </svg>
                            <input
                                value={userName}
                                onChange={(e) => setUserName(e.target.value)}
                                type="text"
                                required
                                placeholder="Username"
                                pattern="[A-Za-z][A-Za-z0-9\-]*"
                                minLength={3}
                                maxLength={30}
                                title="Only letters, numbers or dash"
                            />
                        </label>
                        <p className="validator-hint hidden">
                            Must be 3 to 30 characters
                            <br />containing only letters, numbers or dash
                        </p>
                    </div>
                    <div>
                        <label className="input validator">
                            <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                <g
                                    strokeLinejoin="round"
                                    strokeLinecap="round"
                                    strokeWidth="2.5"
                                    fill="none"
                                    stroke="currentColor"
                                >
                                    <rect width="20" height="16" x="2" y="4" rx="2"></rect>
                                    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                                </g>
                            </svg>
                            <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="mail@site.com" required />
                        </label>
                        <div className="validator-hint hidden">Enter valid email address</div>
                    </div>
                    <div>
                        <label className="input validator">
                            <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                <g
                                    strokeLinejoin="round"
                                    strokeLinecap="round"
                                    strokeWidth="2.5"
                                    fill="none"
                                    stroke="currentColor"
                                >
                                    <path
                                        d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"
                                    ></path>
                                    <circle cx="16.5" cy="7.5" r=".5" fill="currentColor"></circle>
                                </g>
                            </svg>
                            <input
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                type="password"
                                required
                                placeholder="Password"
                                minLength={8}
                                pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                                title="Must be more than 8 characters, including number, lowercase letter, uppercase letter"
                            />
                        </label>
                        <p className="validator-hint hidden">
                            Must be more than 8 characters, including
                            <br />At least one number <br />At least one lowercase letter <br />At least one uppercase letter
                        </p>
                    </div>
                    <button className="btn btn-neutral mt-4">Signup</button>
                </div>
            </form>
        </fieldset>


    )

}