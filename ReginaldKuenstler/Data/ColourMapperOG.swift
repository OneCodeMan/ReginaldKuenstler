//
//  ColourMapping.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-16.
//

import Foundation
import UIKit

struct CatalogColour: Codable, Identifiable {
    let id = UUID() // Unique ID for SwiftUI purposes
    let brand: String
    let name: String
    let rgb: [Int]
}

final class ColourMapper: ObservableObject {
    private(set) var colourMap: [VColour] = []
    static let shared = ColourMapper()
    
    private init() {
        print("ColourMapper init called")
        
        // Wait for both OG and Catalog to finish loading
        ColourMapperOG.shared.createColourMapFromCSV { ogMap in
            ColourCatalog.shared.createColourMapFromCatalogJSON { catalogMap in
                let combinedMap = (ogMap + catalogMap).uniqued()
                DispatchQueue.main.async {
                    self.colourMap = combinedMap
                    // print("ColourMapper combined colourMap: \(self.colourMap)")
                }
            }
        }
    }
}

// MARK: V0.2
final class ColourCatalog: ObservableObject {
    
    // Data
    private(set) var colourMap: [VColour] = []
    
    // Singleton instance
    static let shared = ColourCatalog()
    
    // Prevents external instantiation
    private init() {
        print("ColourCatalog init called")
        self.createColourMapFromCatalogJSON { catalog in
            self.colourMap = catalog
        }
    }
    
    func createColourMapFromCatalogJSON(completion: @escaping ([VColour]) -> Void) {
        print("creating colourMap from JSON.")
        if !colourMap.isEmpty {
            completion(colourMap) // Return existing colourMap if already populated
            return
        }
        
        // Load the JSON data from a file named `catalog.json` in the bundle
       guard let url = Bundle.main.url(forResource: "catalog", withExtension: "json") else {
           print("Could not find catalog.json file.")
           completion([])
           return
       }
       
       do {
           // Read the data from the file
           let data = try Data(contentsOf: url)
        
            // Decode the JSON data into [CatalogColour]
           let catalog: [CatalogColour] = try JSONDecoder().decode([CatalogColour].self, from: data)
           var colours: [VColour] = []
           
           for colour in catalog {
               if colour.rgb.count == 3 {
                   let generatedVColour = VColour(name: colour.name, rgbValue: colour.rgb)
                   colours.append(generatedVColour)
               } else {
                   print("Strangerly, RGB count not 3.")
               }
               
           }
            
            // Update the colourMap and call the completion handler
            DispatchQueue.main.async {
                self.colourMap = colours
                completion(colours)
            }
           } catch {
                      print("Error decoding JSON: \(error)")
                      completion([]) // Return an empty array in case of error
                  }
    }
}



// MARK: V 0.1 colour map.
final class ColourMapperOG: ObservableObject {

    // Data
    private(set) var colourMap: [VColour] = []
    
    // Singleton instance
    static let shared = ColourMapperOG()
    
    // Prevents external instantiation
    private init() {
        print("ColourMapper init called")
        self.createColourMapFromCSV { cM in
            self.colourMap = cM
        }
    }
    
    func createColourMapFromCSV(completion: @escaping ([VColour]) -> Void) {
        print("creating colourMap from CSV.")
        // Check if colourMap is already populated
        if !colourMap.isEmpty {
            completion(colourMap) // Return existing colourMap if already populated
            return
        }
        
        // Proceed to read the CSV and populate colourMap
        var coloursFromCSV: [VColour] = []
        
        guard let filePath = Bundle.main.path(forResource: "colourmap", ofType: "csv") else {
            print("CSV FILE NON-EXISTENT.")
            completion(coloursFromCSV)
            return
        }
        
        DispatchQueue.global(qos: .background).async {
            do {
                let csvData = try String(contentsOfFile: filePath, encoding: .utf8)
                let rows = csvData.components(separatedBy: "\n")
                let rowsWithoutHeaders = rows.dropFirst()
                
                for row in rowsWithoutHeaders {
                    let columns = row.components(separatedBy: ",")
                    
                    if columns.count == 2 {
                        let colourName = columns[0]
                        let hexCode = columns[1]
                        
                        let rgbCode: RGBTuple = ColourHelper.hexToRGB(hex: hexCode)
                        let uiColour: UIColor = UIColor(hex: hexCode)
                        let colour = VColour(name: colourName, hexCode: hexCode, rgbCode: rgbCode, uiColour: uiColour)
                        coloursFromCSV.append(colour)
                    }
                }
                DispatchQueue.main.async {
                    self.colourMap = coloursFromCSV // Store the fetched colours
                    completion(coloursFromCSV)
                }
            } catch {
                print("Error reading CSV file: \(error)")
                DispatchQueue.main.async {
                    completion(coloursFromCSV) // Return empty array on error
                }
            }
        }
    }
}
