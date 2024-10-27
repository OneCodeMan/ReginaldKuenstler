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
                .frame(height: 50)
            Text(paletteColourItem.paletteColour.colourName)
                .bold()
                .strikethrough(paletteColourItem.paletteColour.isUserOwned)
                .foregroundStyle(paletteColourItem.paletteColour.isUserOwned ? .gray : (self.colorScheme == .dark ? .whiteTextLightMode1 : .black))
                .font(.system(size: 14.0))
                .scaledToFill()
                .padding(.top, 3)
        }
        .padding()
        .background(paletteColourItem.paletteColour.isUserOwned ? .gray : .clear)
        .opacity(paletteColourItem.paletteColour.isUserOwned ? 0.3 : (paletteColourItem.isSelected ? 0.4 : 1.0))
        .overlay( /// apply a rounded border
            RoundedRectangle(cornerRadius: 5)
                .stroke(paletteColourItem.isSelected ? .blue : .clear, lineWidth: 0.5)
                .background(paletteColourItem.isSelected ? .blue : .clear)
                .opacity(0.2)
        )
    }
}

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
                .scaledToFill()
                .padding(.top, 3)
        }
        .padding()
        .opacity(paletteColourItem.isUserOwned ? 0.7 : 1.0)
    }
}
