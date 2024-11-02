//
//  AveragePaletteViewModel.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//

import SwiftUI
import Foundation
import SwiftVibrantium

@MainActor
class AveragePaletteViewModel: ObservableObject {
    @Published var paletteResults: [[PaletteColour]] = [] // Array to hold the palettes for each image
    @Published var isLoading: Bool = false

    func analyzeImages(images: [UIImage]) async {
        self.isLoading = true
        self.paletteResults = [] // Clear previous results

        for image in images {
            await analyzeImage(image)
        }

        self.isLoading = false
    }

    private func analyzeImage(_ image: UIImage) async {
        let colourMap = ColourMapper.shared.colourMap
        // Placeholder to store Palette objects for a single image
        var palettesForImage: [PaletteColour] = []

        // Retrieve the color palette using Vibrant
        await withCheckedContinuation { continuation in
            Vibrant.from(image).getPalette { palette in
                let p = palette
                let inputs: [(String, Swatch?)] = [
                    ("Vibrant", p.Vibrant),
                    ("Dark Vibrant", p.DarkVibrant),
                    ("Light Vibrant", p.LightVibrant),
                    ("Muted", p.Muted),
                    ("Light Muted", p.LightMuted),
                    ("Dark Muted", p.DarkMuted)
                ]
                
                // Map each Swatch to a Palette if it exists
                for (_, swatch) in inputs {
                    if let swatch = swatch {
                        let swatchRGB: RGBTuple = ColourHelper.hexToRGB(hex: swatch.hex)
                        let currentVColour = ColourHelper.findNearestColourInMap(withRgbValue: swatchRGB, colourMap: colourMap)
                        let paletteColour = PaletteColour(fromVColour: currentVColour)
                        // let paletteColour = PaletteColour(colourName: name, hexCode: swatch.hex)
                        palettesForImage.append(paletteColour)
                    }
                }

                self.paletteResults.append(palettesForImage) // Store palettes for the image
                continuation.resume()
            }
        }
    }
}
