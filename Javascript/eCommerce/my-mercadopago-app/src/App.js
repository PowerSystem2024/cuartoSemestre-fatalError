import React, { useEffect, useState } from "react";
import { initMercadoPago, Wallet } from "@mercadopago/sdk-react";

// Inicializa Mercado Pago con tu Public Key
initMercadoPago("APP_USR-84f9c12d-a4f5-4398-b2aa-cbb495a704b6", { locale: "es-AR" });

const App = () => {
  const [preferenceId, setPreferenceId] = useState(null);

  useEffect(() => {
    const createPreference = async () => {
      try {
        const res = await fetch("http://localhost:3000/create_preference", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            items: [
              {
                title: "Mi producto",
                quantity: 1,
                unit_price: 2000,
              },
            ],
          }),
        });

        if (!res.ok) throw new Error("Error creando preferencia");

        const data = await res.json();
        console.log("Preference creada:", data);
        setPreferenceId(data.preference_id);
      } catch (error) {
        console.error("Error creando preferencia:", error);
      }
    };

    createPreference();
  }, []);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "50px",
      }}
    >
      <h1>Botón de Pago</h1>
      <p>Haz clic en el botón para realizar el pago.</p>

      {/* Renderiza el botón de pago solo si existe un preferenceId */}
      {preferenceId && <div style={{ width: "300px" }}>
        {preferenceId ? (
          <Wallet initialization={{ preferenceId: preferenceId }} />
        ) : (
          <p>Cargando botón de pago...</p>
        )}
      </div>}
    </div>
  );
};

export default App;
