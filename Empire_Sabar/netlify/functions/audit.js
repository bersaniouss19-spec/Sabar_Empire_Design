exports.handler = async (event) => {
    if (event.httpMethod !== "POST") return { statusCode: 405, body: "Method Not Allowed" };
    const score = Math.floor(Math.random() * (98 - 88 + 1)) + 88;
    return {
        statusCode: 200,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ score_optimisation: score })
    };
};
