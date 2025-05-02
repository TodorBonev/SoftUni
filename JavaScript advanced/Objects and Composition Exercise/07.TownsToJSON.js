function tableToJSON(inputData) {

    const dataRows = inputData.slice(1);
    const result = [];
    
    for (const row of dataRows) {

      const columns = row.split('|').filter(item => item.trim()).map(item => item.trim());
      
      const town = columns[0];

      const latitude = parseFloat((parseFloat(columns[1])).toFixed(2));
      const longitude = parseFloat((parseFloat(columns[2])).toFixed(2));
      
      result.push({
        Town: town,
        Latitude: latitude,
        Longitude: longitude
      });
    }
    
    return JSON.stringify(result);
  }
  

