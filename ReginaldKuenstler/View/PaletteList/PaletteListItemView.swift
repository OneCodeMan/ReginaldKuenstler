//
//  PaletteListItemView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct PaletteListItemView: View {
    @Binding var paletteColourItem: PaletteColourSelectItem
    
    // MARK: light vs. dark mode
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        VStack {
            Circle()
                .stroke(.gray, lineWidth: 2)
                .fill(Color(paletteColourItem.paletteColour.uiColour))
                .frame(height: 45)
            
            Text(paletteColourItem.paletteColour.colourName)
                .bold()
                .strikethrough(paletteColourItem.paletteColour.isUserOwned)
                .foregroundStyle(paletteColourItem.paletteColour.isUserOwned ? .gray : (self.colorScheme == .dark ? .whiteTextLightMode1 : .black))
                .font(.system(size: 13.0))
                .multilineTextAlignment(.center) // Center align text for better appearance
                .lineLimit(2)
                .frame(maxWidth: .infinity)
                .padding(5)
        }
        .padding(10) // Overall padding
        .background(paletteColourItem.paletteColour.isUserOwned ? .gray : .clear)
        .opacity(paletteColourItem.paletteColour.isUserOwned ? 0.3 : (paletteColourItem.isSelected ? 0.4 : 1.0))
        .overlay(
            RoundedRectangle(cornerRadius: 5)
                .stroke(paletteColourItem.isSelected ? .blue : .clear, lineWidth: 0.2)
                .background(paletteColourItem.isSelected ? .blue.opacity(0.2) : .clear) // Adjust background opacity
        )
    }
}

// MARK: UserPaletteListItemView
struct UserPaletteListItemView: View {
    @State var paletteColourItem: PaletteColour
    
    var body: some View {
        VStack {
            Circle()
                .stroke(.gray, lineWidth: 2)
                .fill(Color(paletteColourItem.uiColour))
                .frame(height: 50)
            
            Text(paletteColourItem.colourName)
                .bold()
                .font(.system(size: 14.0))
                .multilineTextAlignment(.center) // Center align text for better appearance
                .lineLimit(2)
                .frame(maxWidth: .infinity)
                .padding(5)
        }
        .padding(10) // Overall padding
        .opacity(paletteColourItem.isUserOwned ? 0.7 : 1.0)
    }
}

