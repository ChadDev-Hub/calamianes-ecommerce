import ThemeSwitch from "./themeswitch"
export default function Navbar(props:any) {
    return (
        <div className="navbar flex justify-between bg-base-200 shadow-sm">
            <div className="ps-3">
                <a className="btn btn-ghost text-xl">{props.title}</a>
            </div>
            <div className="pe-3">
                <ThemeSwitch/>
            </div>
        </div>
    )
}