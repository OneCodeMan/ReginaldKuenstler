//
//  ReginaldKuenstlerApp.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-15.
//

import SwiftUI

@main
struct ReginaldKuenstlerApp: App {
    // @StateObject private var colourMapper = ColourMapper()
    @StateObject private var userPaletteViewModel = UserPaletteViewModel()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(userPaletteViewModel)
        }
    }
}
