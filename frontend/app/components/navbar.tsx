import ThemeSwitch from "./themeswitch"
interface NavbarProps{
    title: string
}
export default function Navbar(props:NavbarProps) {
    return (
        <div className="navbar  fixed flex justify-between bg-base-200 shadow-sm">
            <div className="ps-3">
                <a className="btn btn-ghost text-xl">{props.title}</a>
            </div>
            <div className="pe-3">
                <ThemeSwitch/>
            </div>  
        </div>
    )
}