//
//  ReginaldKuenstlerApp.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-15.
//

import SwiftUI

@main
struct ReginaldKuenstlerApp: App {
    @StateObject private var userPaletteData = UserPaletteData()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(userPaletteData)
        }
    }
}
