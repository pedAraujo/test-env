import React, { useState, useEffect } from "react"

function App() {
	const [data, setData] = useState([{}])

	useEffect((data) => {
		fetch("/")
			.then((res) => res.json())
			.then((data) => setData(data))
		console.log(data)
	}, [])
	// empty array as second argument so it only runs once

	return (
		<div>
			{typeof data.messages === "undefined" ? (
				<p>Loading...</p>
			) : (
				data.messages.map((message, i) => <p key={i}>{message}</p>)
			)}
		</div>
	)
}

export default App
