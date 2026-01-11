import { homepageData } from "./service/api";
import Landing from "./landing";
export default async function Home() {
  const data = await homepageData.data()
  return ( 
    <div className="flex min-h-screen items-center justify-center  font-sans">
      <main className="flex min-h-screen w-full flex-col justify-between content-center">
        <Landing data={data}/>
      </main>
    </div>
  );
};
