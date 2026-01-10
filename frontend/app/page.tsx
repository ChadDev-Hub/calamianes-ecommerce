import ThemeSwitch from "./components/themeswitch";
import { homepageData } from "./service/api";
import Navbar from "./components/navbar";
export default async function Home() {
  const data = await homepageData.data()
  return (
    <div className="flex min-h-screen items-center justify-center  font-sans">
      <main className="flex min-h-screen w-full flex-col items-center justify-between">
        <Navbar title={"Welcome to Calamian Ecommerce"}/>
        <div className="flex b-black flex-col gap-6  tracking-tigh">
          <h1 className="max-w-xs text-3xl font-semibold   tracking-tight ">
            {data.title}
          </h1>
          <p className="max-w-md text-lg  ">
            {data.description}
          </p>
        </div>
      </main>
    </div>
  );
};
