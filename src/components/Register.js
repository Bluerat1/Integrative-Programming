import React, { useEffect, useState } from 'react';
import api from '../api';

export default function Dashboard() {
  const [readings, setReadings] = useState([]);

  useEffect(() => {
    api.get('sensor-reading/')
      .then(res => setReadings(res.data))
      .catch(console.error);
  }, []);

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-2xl mb-4">Sensor Readings</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-2">Device</th>
              <th className="p-2">Voltage (V)</th>
              <th className="p-2">Current (A)</th>
              <th className="p-2">Power (W)</th>
              <th className="p-2">Energy (kWh)</th>
            </tr>
          </thead>
          <tbody>
            {readings.map((r, i) => (
              <tr key={i} className="border-t">
                <td className="p-2">{r.device_name}</td>
                <td className="p-2">{r.voltage.toFixed(2)}</td>
                <td className="p-2">{r.current.toFixed(4)}</n    <td className="p-2">{r.power.toFixed(4)}</td>
                <td className="p-2">{r.energy.toFixed(4)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
}