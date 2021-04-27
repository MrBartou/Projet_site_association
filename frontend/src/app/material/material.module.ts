import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { MatTabsModule } from '@angular/material/tabs'
import { MatSidenavModule } from '@angular/material/sidenav'
import { MatToolbarModule } from '@angular/material/toolbar'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatListModule } from '@angular/material/list'
import { FlexLayoutModule } from '@angular/flex-layout'

@NgModule({
    declarations: [],
    imports: [
        CommonModule,
        MatTabsModule,
        MatSidenavModule,
        MatToolbarModule,
        MatIconModule,
        MatButtonModule,
        MatListModule,
        FlexLayoutModule
    ],
    exports: [
        MatTabsModule,
        MatSidenavModule,
        MatToolbarModule,
        MatIconModule,
        MatButtonModule,
        MatListModule
    ]
})

export class MaterialModule { }