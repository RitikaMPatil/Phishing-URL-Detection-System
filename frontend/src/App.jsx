import { useState } from "react";
import axios from "axios";

function App() {

  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");

  const checkURL = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/predict",
        {
          url,
        }
      );

      setResult(response.data.prediction);

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen bg-black flex items-center justify-center text-white">

      <div className="bg-gray-900 p-10 rounded-2xl shadow-lg w-[500px]">

        <h1 className="text-3xl font-bold text-center mb-6">
          Phishing URL Detection System
        </h1>

        <input
          type="text"
          placeholder="Enter URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="w-full p-3 rounded-lg text-black"
        />

        <button
          onClick={checkURL}
          className="w-full bg-blue-500 mt-4 p-3 rounded-lg hover:bg-blue-600"
        >
          Check URL
        </button>

        {result && (
          <div className="mt-6 text-center text-2xl font-semibold">
            {result}
          </div>
        )}

      </div>

    </div>
  );
}

export default App;